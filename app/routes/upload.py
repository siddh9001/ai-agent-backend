from fastapi import APIRouter, UploadFile, BackgroundTasks
from fastapi.responses import RedirectResponse
from app.services.file_service import save_uploaded_file
from app.services.embed_service import process_file_embeddings
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/upload")
def upload_get():
    return RedirectResponse(url="/", status_code=302)

@router.post("/upload")
async def upload(file: UploadFile, background: BackgroundTasks):
    try:
        saved_path = await save_uploaded_file(file)
        
        if not saved_path:
            logger.error("File save failed")
            return {
                "status": "Failed",
                "message": "Failed to save the uploaded file"
            }
        
        background.add_task(process_file_embeddings, saved_path)

        return {
            "status": "File uploaded successfully",
            "file_path": saved_path,
            "message": "Embedding generation started in background"
        }
    except Exception as e:
        logger.error(f"Upload error: {str(e)}")
        return {
            "status": "Failed",
            "message": f"Upload failed: {str(e)}"
        }