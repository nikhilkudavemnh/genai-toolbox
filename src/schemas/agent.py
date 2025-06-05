from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AgentBase(BaseModel):
    name: str
    description: Optional[str] = None

class AgentCreate(AgentBase):
    pass

class AgentResponse(AgentBase):
    id: int
    status: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True