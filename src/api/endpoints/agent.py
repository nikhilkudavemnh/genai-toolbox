from fastapi import APIRouter, Depends
from typing import List
from schemas.agent import AgentCreate, AgentResponse
from services.agent_service import AgentService

router = APIRouter()

@router.post("/agents", response_model=AgentResponse, tags=["Agents"])
async def create_agent(agent: AgentCreate):
    """Create a new agent"""
    # Implementation will be added later
    return {"id": 1, "name": agent.name, "status": "created"}

@router.get("/agents", response_model=List[AgentResponse], tags=["Agents"])
async def list_agents():
    """List all agents"""
    # Implementation will be added later
    return []

@router.get("/agents/{agent_id}", response_model=AgentResponse, tags=["Agents"])
async def get_agent(agent_id: int):
    """Get agent by ID"""
    # Implementation will be added later
    return {"id": agent_id, "name": "Sample Agent", "status": "active"}