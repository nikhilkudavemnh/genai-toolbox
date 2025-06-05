from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "My FastAPI Application"
    debug: bool = False
    database_url: Optional[str] = None
    redis_url: Optional[str] = "redis://localhost:6379"
    secret_key: str = "your-secret-key-here"
    
    class Config:
        env_file = ".env"

settings = Settings()