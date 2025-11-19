from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from app.core.config import settings

embedding_model = HuggingFaceEmbeddings(
    model_name=settings.EMBEDDING_MODEL
)

vector_store = Chroma(
    collection_name="example_collection",
    persist_directory=settings.VECTOR_DB_PATH,
    embedding_function=embedding_model
)