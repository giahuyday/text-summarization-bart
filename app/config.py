from pydantic import BaseSettings

class Settings(BaseSettings):
    model_path: str = "path/to/bert_model"

    class Config:
        env_file = ".env"

settings = Settings()
