from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    VECTOR_DB_PATH: str = "data/vector_db/"
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    model_config = SettingsConfigDict(
        env_file = ".env"
    )

settings = Settings()