from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse
from app.services.embed_service import embed_text
from app.services.search_service import search_similar_text
router = APIRouter()

@router.get("/chat")
def chat_get():
    return RedirectResponse(url="/", status_code=302)

@router.post("/chat")
def chat(chat: str = Form(...)):
    embedding = embed_text(chat)
    similar_text = search_similar_text(embedding)
    return {"chat": chat, "similar_text": similar_text}