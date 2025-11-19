from app.core.models import embedding_model, vector_store
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
import logging

logger = logging.getLogger(__name__)

def process_file_embeddings(file_path: str):
    print(file_path)
    try:
        text = Path(file_path).read_text(encoding='utf-8', errors='ignore')

        splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=10)
        chunks = splitter.split_text(text)

        embeddings = embedding_model.embed_documents(chunks)

        vector_store.add_texts(texts=text, metadatas=[{"file": file_path}]* len(chunks), embeddings=embeddings)

        logger.info(f"Embeddings stored | {file_path} | {len(chunks)} chunks")
    except Exception as e:
        logger.error("Embeddings store error: ", str(e))
