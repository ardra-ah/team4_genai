from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    claude_api_key: str = "mock-api-key"
    gemini_api_key: str = "mock-api-key"
    database_url: str = "sqlite:///claims.db"
    upload_dir: str = "./uploads"
    log_level: str = "INFO"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_reload: bool = True
    use_rag: bool = True
    use_gemini: bool = False
    policy_vector_store: str = "./data/policies_vectorstore"

    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "allow"


settings = Settings()
