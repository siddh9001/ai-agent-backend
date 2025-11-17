from pydantic import BaseSettings

class Settings(BaseSettings):
    VECTOR_DB_PATH: str = "data/vector_db/"
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    class Config:
        env_file = ".env"

settings = Settings()