# mypy: disable-error-code=import-untyped
from typing import Any, cast
import os
import time
from pathlib import Path
import whisper
from whisper.model import Whisper
from redis import Redis
from celery import Celery
from celery.result import AsyncResult
from celery.signals import after_task_publish
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

redis = Redis(host="redis", port=6379, db=0)


@after_task_publish.connect # type: ignore
def store_task_id(headers: dict[str, Any] | None = None, **kwargs: Any) -> None:
    if headers:
        task_id = headers.get("id")
        redis.set(f"task_{task_id}", 1, ex=10800)
        print(f"[LOG] Stored task {task_id} in Redis!")
    else:
        print("[LOG] Failed to store task!")


@app.task(bind=True, track_started=True) # type: ignore
def transcribe(self: Any, audio_path: str) -> str:
    print(f"[LOG] Received '{audio_path}', starting transcription processs...")
    result = cast(Whisper, model).transcribe(audio_path)
    result_text = result["text"].strip()
    print(f"[LOG] Finished transcribing '{audio_path}', saving results in a file...")
    filename = Path(audio_path).stem
    transcription_file_path = StorageService.save_transcription_result(
        filename=f"{filename}.txt",
        result=result_text
    )
    clear_transcription_files_and_metadata.apply_async(args=(self.request.id,), countdown=60)
    return str(transcription_file_path)

def find_audio_file_path_by_stem(stem: str) -> Path:
    audio_dir_path = StorageService.data_dir_path / StorageService.audio_dir_name
    for audio_file_path in audio_dir_path.iterdir():
        if audio_file_path.stem == stem:
            return audio_file_path
    raise FileNotFoundError(f"Audio with stem '{stem}' was not found")

@app.task # type: ignore
def clear_transcription_files_and_metadata(task_id: str) -> None:
    time.sleep(.1)
    try:
        task: AsyncResult = app.AsyncResult(task_id)
        transcription_file_path = Path(cast(str, task.result))
        audio_file_path = find_audio_file_path_by_stem(transcription_file_path.stem)
        audio_file_path.unlink()
        transcription_file_path.unlink()
        redis.delete(f"task_{task_id}")
        print(f"[LOG] Deleted task {task_id} from Redis!")
    except FileNotFoundError:
        print(f"[LOG] Tried to delete {task_id} files and metadata, but they had already been deleted.")