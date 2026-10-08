from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "qwen-tts-api"
    app_version: str = "0.1.0"

    host: str = "0.0.0.0"
    port: int = 8000

    model_name: str = "Qwen/Qwen3-TTS"
    device: str = "cuda"

    class Config:
        env_file = ".env"


settings = Settings()