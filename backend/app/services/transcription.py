from fastapi import UploadFile
from app.worker.tasks import transcribe
from app.services.storage import StorageService

class TranscriptionService:
    @staticmethod
    async def request_transcription(audio: UploadFile) -> str:
        audio_path = await StorageService.save_uploaded_audio(audio)
        task = transcribe.delay(str(audio_path))
        return task.id