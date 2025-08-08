from pydantic import BaseModel, Field

class TenantCreate(BaseModel):
    tenant_id :int
    name: str