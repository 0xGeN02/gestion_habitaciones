from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://gestion_salas_user:1234@localhost:5432/gestion_salas_db"

settings = Settings()
