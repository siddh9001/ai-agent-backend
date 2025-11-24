from app.core.models import embedding_model, vector_store
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

def process_file_embeddings(file_path: str):
    print(f"Processing file: {file_path}")
    try:
        loader = TextLoader(file_path, encoding='utf-8')
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(documents)

        vector_store.add_documents(documents=chunks)

        print(f"Embeddings stored | {file_path} | {len(chunks)} chunks")
    except Exception as e:
        print("Embeddings store error: ", str(e))

def embed_text(text: str):
    try:
        embedding = embedding_model.embed_query(text)
        return embedding
    except Exception as e:
        print("Embedding error: ", str(e))
        return None
