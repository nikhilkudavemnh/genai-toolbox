from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from rich import print as rprint
from src.db.session import engine
import time


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield  # App is now running
    engine.dispose()



app = FastAPI(
    title="🎨 Generative AI API",
    description="Interact with cutting-edge AI endpoints.",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["Monitoring"])
async def health_check():
    return {"statusCode": 200, "message": "Healthy 🎉"}


@app.get("/health-full", tags=["Monitoring"])
async def health_check_full(include_version: bool = Query(True, description="Include version info?")):
    data = {
        "statusCode": 200,
        "message": "API is running ✔️"
    }
    if include_version:
        data["version"] = "1.0.0"
    return data




if __name__ == "__main__":
    import uvicorn
    import asyncio

    uvicorn.run(app, host="0.0.0.0", port=8098)
