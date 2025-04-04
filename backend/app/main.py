from fastapi import FastAPI, UploadFile, HTTPException
from app.services.transcription import TranscriptionService

app = FastAPI()

@app.post("/transcriptions")
async def request_transcription(audio: UploadFile) -> dict[str, str]:
    if not audio.filename:
        raise HTTPException(status_code=400, detail="Filename is missing")
    task_id = await TranscriptionService.request_transcription(audio)
    return {"task_id": task_id}