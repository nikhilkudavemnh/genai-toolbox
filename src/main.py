from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from api.endpoints import health, agent
from config import settings
from score.logging import logger

app = FastAPI(
    title=settings.app_name,
    description="This is a sample FastAPI application with modular structure.",
    debug=settings.debug
)

# Include routers
app.include_router(health.router, prefix="/api/v1")
app.include_router(agent.router, prefix="/api/v1")

@asynccontextmanager
def lifespan(app: FastAPI):
    """Application lifespan context manager for startup and shutdown events."""
    logger.info("Starting application...")
    yield
    logger.info("Shutting down application...")

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=5004,
        reload=True
    )