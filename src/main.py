from fastapi import FastAPI

from api.routes import health, tts


def create_app() -> FastAPI:
    app = FastAPI(
        title="Qwen TTS API",
        version="0.1.0",
    )

    app.include_router(health.router)
    app.include_router(tts.router)

    return app


app = create_app()