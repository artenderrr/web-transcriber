from typing import Annotated, cast
from fastapi import FastAPI, Path, UploadFile, Depends, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from redis import Redis
from celery.result import AsyncResult # type: ignore
from app.core import get_cors_settings
from app.worker import worker
from app.worker.tasks import clear_transcription_files_and_metadata
from app.services.transcription import TranscriptionService


app = FastAPI(title="Transcription API")
app.add_middleware(CORSMiddleware, **get_cors_settings())

redis = Redis(host="redis", port=6379, db=0)


def existing_task(task_id: Annotated[str, Path()]) -> AsyncResult:
    if not redis.exists(f"task_{task_id}"):
        raise HTTPException(status_code=404, detail="Task with provided ID doesn't exist")
    task: AsyncResult = worker.AsyncResult(task_id)
    return task

ExistingTask = Annotated[AsyncResult, Depends(existing_task)]


@app.post("/transcriptions")
async def request_transcription(audio: UploadFile) -> dict[str, str]:
    if not audio.filename:
        raise HTTPException(status_code=400, detail="Filename is missing")
    task_id = await TranscriptionService.request_transcription(audio)
    return {"task_id": task_id}

@app.get("/transcriptions/{task_id}")
def get_transcription_result(task: ExistingTask) -> FileResponse:
    if task.state != "SUCCESS":
        raise HTTPException(status_code=202, detail="Transcription is still in progress.")
    transcription_file_path = cast(str, task.result)
    clear_transcription_files_and_metadata.delay(task.id)
    return FileResponse(transcription_file_path)

@app.get("/transcriptions/{task_id}/state")
def check_transcription_state(task: ExistingTask) -> dict[str, str]:
    return {"state": task.state}