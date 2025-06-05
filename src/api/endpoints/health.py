from fastapi import APIRouter

router = APIRouter()

@router.get("/heartbeat", tags=["Health Check"])
async def heartbeat():
    return {"status": "alive"}

@router.get("/health", tags=["Health Check"])
async def health_check():
    return {
        "status": "healthy",
        "service": "FastAPI Application"
    }