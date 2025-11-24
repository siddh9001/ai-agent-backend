from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def home():
    logger.info("Home page accessed")
    return """
    <html>
        <body>
            <h2>Upload a file</h2>
            <form action="/upload" enctype="multipart/form-data" method="post">
                <input name="file" type="file" />
                <button type="submit">Upload</button>
            </form>
            <form action="/chat" enctype="application/x-www-form-urlencoded" method="post">
                <input name="chat" type="text" />
                <button type="submit">Chat</button>
            </form>
        </body>
    </html>
    """
