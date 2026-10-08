from fastapi import APIRouter

from schemas.health import HealthResponse


router = APIRouter(
    prefix="/health",
    tags=["health"],
)


@router.get("", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="ok",
    )
    
    
@router.get("/info")
async def info():
    return {
        "service": "qwen-tts-api",
        "version": "0.1.0",
    }