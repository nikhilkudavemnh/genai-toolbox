from fastapi import APIRouter
from sqlalchemy import text
from src.schemas.tenant_schemas import TenantCreate
from src.db.session import engine

tenant_routes = APIRouter()

@tenant_routes.post("/create", )
async def create_tenant(data: TenantCreate):
    schema_name = f"employer_db_{data.tenant_id}"
    async with engine.begin() as conn:
        await conn.execute(text(f'CREATE SCHEMA IF NOT EXISTS "{schema_name}"'))
        await conn.execute(text(f"""
            INSERT INTO public.tenants (tenant_id, name, schema_name)
            VALUES (:tenant_id, :name, :schema_name)
            ON CONFLICT (tenant_id) DO UPDATE SET
                name = EXCLUDED.name,
                schema_name = EXCLUDED.schema_name
        """), {
            "tenant_id": int(data.tenant_id),
            "name": data.name,
            "schema_name": schema_name,
        })
    return data.model_dump()
        # Optionally run migrations for the new schema

a