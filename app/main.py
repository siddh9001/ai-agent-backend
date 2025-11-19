from fastapi import FastAPI
from app.routes.home import router as home_router
from app.routes.upload import router as upload_router

app = FastAPI(title="AI Agent Backend")

# mount routes
app.include_router(home_router)
app.include_router(upload_router)