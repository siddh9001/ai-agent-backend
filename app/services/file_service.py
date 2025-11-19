import logging
from pathlib import Path
from fastapi import UploadFile

logger = logging.getLogger(__name__)
BASE_DIR = Path('data/docs')

async def save_uploaded_file(file: UploadFile) -> str:
    try:
        BASE_DIR.mkdir(parents=True, exist_ok=True)
        file_path = BASE_DIR / file.filename
        with open(file_path, "wb") as f:
            f.write(await file.read())

        logger.info(f"File saved successfully: {file_path}")
        return str(file_path)
    except Exception as e:
        logger.error(f"Error saving file {file.filename}: {str(e)}")
        return ""