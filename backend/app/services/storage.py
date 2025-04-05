from typing import cast
import os
from pathlib import Path
from fastapi import UploadFile

class StorageService:
    data_dir_path = Path("/data")
    audio_dir_name = "audio"
    transcription_dir_name = "transcriptions"
    
    @staticmethod
    def _save_content_as_file(*, filename: str, location: Path, content: str | bytes) -> Path:
        if not isinstance(content, (str, bytes)):
            raise TypeError("Content must be of type str or bytes")
        file_path = location / filename
        mode = "wb" if isinstance(content, bytes) else "w"
        os.makedirs(location, exist_ok=True)
        with open(file_path, mode) as file:
            file.write(content)
        return file_path
    
    @staticmethod
    async def save_uploaded_audio(audio: UploadFile) -> Path:
        audio_content = await audio.read()
        audio_dir_path = (
            StorageService.data_dir_path / StorageService.audio_dir_name
        )
        audio_file_path = StorageService._save_content_as_file(
            filename=cast(str, audio.filename),
            location=audio_dir_path,
            content=audio_content
        )
        return audio_file_path
    
    @staticmethod
    def save_transcription_result(*, filename: str, result: str) -> Path:
        transcription_dir_path = (
            StorageService.data_dir_path / StorageService.transcription_dir_name
        )
        transcription_file_path = StorageService._save_content_as_file(
            filename=filename,
            location=transcription_dir_path,
            content=result
        )
        return transcription_file_path