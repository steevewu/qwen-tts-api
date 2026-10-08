import uvicorn

from core.config import settings


if __name__ == "__main__":
    uvicorn.run(
        "qwen_tts_api.main:app",
        host=settings.host,
        port=settings.port,
        reload=False,
    )