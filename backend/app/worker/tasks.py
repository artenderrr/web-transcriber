from typing import cast
import os
import time
from pathlib import Path
import whisper # type: ignore
from whisper.model import Whisper # type: ignore
from celery import Celery
from celery.result import AsyncResult
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
def transcribe(audio_path: str) -> str:
    print(f"[LOG] Received '{audio_path}', starting transcription processs...")
    result = cast(Whisper, model).transcribe(audio_path)
    print(f"[LOG] Finished transcribing '{audio_path}', saving results in a file...")
    filename = Path(audio_path).stem
    transcription_file_path = StorageService.save_transcription_result(
        filename=f"{filename}.txt",
        result=result["text"]
    )
    return str(transcription_file_path)

def find_audio_file_path_by_stem(stem: str) -> Path:
    audio_dir_path = StorageService.data_dir_path / StorageService.audio_dir_name
    for audio_file_path in audio_dir_path.iterdir():
        if audio_file_path.stem == stem:
            return audio_file_path
    raise FileNotFoundError(f"Audio with stem '{stem}' was not found")

@app.task
def clear_transcription_files(task_id: str) -> None:
    time.sleep(.1)
    task: AsyncResult[None] = app.AsyncResult(task_id)
    transcription_file_path = Path(cast(str, task.result))
    audio_file_path = find_audio_file_path_by_stem(transcription_file_path.stem)
    audio_file_path.unlink()
    transcription_file_path.unlink()