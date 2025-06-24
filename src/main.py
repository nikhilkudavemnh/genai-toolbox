from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import time
from .logger import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application starting up...")
    yield
    logger.info("Application shutting down...")

app = FastAPI(lifespan=lifespan)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    try:
        response = await call_next(request)
        process_time = round((time.time() - start_time) * 1000, 2)
        
        # Log successful request
        logger.info("Request processed", extra={
            "method": request.method,
            "url": str(request.url),
            "status_code": response.status_code,
            "process_time_ms": process_time,
            "client_ip": request.client.host if request.client else None,
            "user_agent": request.headers.get("user-agent", "Unknown")
        })
        
    except Exception as e:
        process_time = round((time.time() - start_time) * 1000, 2)
        
        # Log error request with full traceback
        logger.exception("Request processed with error", extra={
            "method": request.method,
            "url": str(request.url),
            "status_code": 500,
            "process_time_ms": process_time,
            "client_ip": request.client.host if request.client else None,
            "user_agent": request.headers.get("user-agent", "Unknown"),
            "error": str(e)
        })
        
        response = JSONResponse(
            status_code=500,
            content={"status": 500, "error": "Internal server error"}
        )

    return response

@app.get("/")
async def read_root():
    # Fixed the division by zero error for testing
    return {"status": "success", "message": "API is running"}

@app.get("/test-error")
async def test_error():
    # Moved the error to a separate endpoint for testing
    b = 100 / 0 
    return {"status": b}