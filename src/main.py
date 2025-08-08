from contextlib import asynccontextmanager

from fastapi import FastAPI, Query
from fastapi import Request, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import text
from fastapi.exceptions import HTTPException
from src.apis.v1.tenant_routes import tenant_routes
from src.db.base import Base
from src.db.session import engine
from src.utils.tenant_util import get_schema_name


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


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

def get_tenant_id(x_tenant_id: str = Header(...)):
    # Optionally validate the tenant ID
    if not x_tenant_id:
        raise HTTPException(status_code=400, detail="X-Tenant-ID header missing")
    return x_tenant_id

app.include_router(
    tenant_routes,
    prefix="/v1/tenants",
    tags=["Tenants"],
    dependencies=[Depends(get_tenant_id)]
)
@app.middleware("http")
async def set_tenant_schema(request: Request, call_next):
    excluded_urls = ["/health", "/health-full","/docs", "/openapi.json"]
    if request.url.path in excluded_urls:
        response = await call_next(request)
        return response
    tenant_id = request.headers.get("X-Tenant-ID")
    if not tenant_id:
        return JSONResponse({"error": "Missing tenant ID"}, status_code=400)

    schema_name = await get_schema_name(int(tenant_id))
    if not schema_name and request.url.path == '/v1/tenants/create':
        response = await call_next(request)
        return response

    async with engine.begin() as conn:
        await conn.execute(text(f"SET search_path TO {schema_name}, public"))
        request.state.db = conn
        response = await call_next(request)
        return response



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
    uvicorn.run(app, host="0.0.0.0", port=8098)
