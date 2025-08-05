from pydantic_settings import  BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:1234@localhost:5432/genai-toolbox"
    API_VERSION: str = "1.0.0"

    class Config:
        env_file = ".env"



settings =  Settings()