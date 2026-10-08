from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/tts",
    tags=["tts"],
)


@router.post("")
async def generate_tts():
    raise HTTPException(
        status_code=501,
        detail="TTS generation is not implemented yet",
    )