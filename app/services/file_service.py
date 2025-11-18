from pathlib import Path
from fastapi import UploadFile

BASE_DIR = Path('data/docs')

async def save_uploaded_file(file: UploadFile) -> str:
    BASE_DIR.mkdir(parents=True, exist_ok=True)

    file_path = BASE_DIR / file.filename

    with open(file_path, "wb") as f:
        f.write(await file.read())

    return str(file_path)