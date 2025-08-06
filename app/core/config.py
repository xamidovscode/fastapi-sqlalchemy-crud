from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Boilerplate"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "postgresql+asyncpg://db_user:password@host:port/db_name"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()

