from typing import cast
import os
from pathlib import Path
import whisper # type: ignore
from whisper.model import Whisper # type: ignore
from celery import Celery
from app.services.storage import StorageService

app = Celery(
    "tasks",
    broker="amqp://rabbitmq",
    backend="redis://redis"
)

def load_model() -> Whisper | None:
    print(f"[LOG] CELERY_WORKER_RUNNING = {os.getenv('CELERY_WORKER_RUNNING')}")
    if os.getenv("CELERY_WORKER_RUNNING"):
        print("[LOG] Loading model...")
        model = whisper.load_model("small")
        print("[LOG] Model is loaded!")
        return model
    return None

model = load_model()

@app.task(track_started=True)
def transcribe(audio_path: str) -> None:
    print(f"[LOG] Received '{audio_path}', starting transcription processs...")
    result = cast(Whisper, model).transcribe(audio_path)
    print(f"[LOG] Finished transcribing '{audio_path}', saving results in a file...")
    filename = Path(audio_path).stem
    StorageService.save_transcription_result(
        filename=f"{filename}.txt",
        result=result["text"]
    )