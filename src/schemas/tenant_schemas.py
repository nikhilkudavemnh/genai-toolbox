from pydantic import BaseModel, Field

class TenantCreate(BaseModel):
    id :int
    name: str