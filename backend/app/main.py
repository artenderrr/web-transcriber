from typing import cast
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
from celery.result import AsyncResult
from app.worker import worker
from app.worker.tasks import clear_transcription_files
from app.services.transcription import TranscriptionService

app = FastAPI()

@app.post("/transcriptions")
async def request_transcription(audio: UploadFile) -> dict[str, str]:
    if not audio.filename:
        raise HTTPException(status_code=400, detail="Filename is missing")
    task_id = await TranscriptionService.request_transcription(audio)
    return {"task_id": task_id}

@app.get("/transcriptions/{task_id}")
def get_transcription_result(task_id: str) -> FileResponse:
    task: AsyncResult[None] = worker.AsyncResult(task_id)
    try:
        transcription_file_path = cast(str, task.result)
    except AttributeError:
        raise HTTPException(status_code=404, detail="Task with provided ID doesn't exist")
    clear_transcription_files.delay(task_id)
    return FileResponse(transcription_file_path)

@app.get("/transcriptions/{task_id}/state")
def check_transcription_state(task_id: str) -> dict[str, str]:
    task: AsyncResult[None] = worker.AsyncResult(task_id)
    try:
        state = task.state
    except AttributeError:
        raise HTTPException(status_code=404, detail="Task with provided ID doesn't exist")
    return {"state": state}