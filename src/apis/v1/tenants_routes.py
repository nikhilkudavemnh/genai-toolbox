from fastapi import APIRouter
from sqlalchemy import text
from src.schemas.tenant_schemas import TenantCreate
from src.db.session import engine

tenant_routes = APIRouter(prefix="v1")

@tenant_routes.post("/create_tenant", response_model=TenantCreate)
async def create_tenant(data: TenantCreate):
    schema_name = f"employer_db_{data.tenant_id}"
    async with engine.begin() as conn:
        await conn.execute(text(f'CREATE SCHEMA IF NOT EXISTS "{schema_name}"'))
        await conn.execute(text(f"""
            INSERT INTO public.tenants (tenant_id, name, schema_name)
            VALUES (:tenant_id, :name, :schema_name)
        """), {
            "tenant_id": data.tenant_id,
            "name": data.name,
            "schema_name": schema_name,
        })
    return TenantCreate
        # Optionally run migrations for the new schema
