from src.db.session import engine
from sqlalchemy import text
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse


async def get_schema_name(tenant_id: int) -> str | None:
    query = text("SELECT schema_name FROM public.tenants WHERE tenant_id = :tenant_id")
    async with engine.connect() as conn:
        result = await conn.execute(query, {"tenant_id": tenant_id})
        row = result.fetchone()
        if row:
            return row[0]
        return None
