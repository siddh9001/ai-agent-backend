from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from app.core.config import settings

embedding_model = HuggingFaceEmbeddings(
    model_name=settings.EMBEDDING_MODEL
)

vector_store = Chroma(
    persist_directory=settings.VECTOR_DB_PATH,
    embedding_function=embedding_model
)