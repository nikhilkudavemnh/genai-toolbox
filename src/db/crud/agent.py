from sqlalchemy.orm import Session
from typing import List, Optional
from src.db.models.agent import Agent
from src.schemas.agent import AgentCreate

def get_agent(db: Session, agent_id: int) -> Optional[Agent]:
    return db.query(Agent).filter(Agent.id == agent_id).first()

def get_agents(db: Session, skip: int = 0, limit: int = 100) -> List[Agent]:
    return db.query(Agent).offset(skip).limit(limit).all()

def create_agent(db: Session, agent: AgentCreate) -> Agent:
    db_agent = Agent(**agent.dict())
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent

def delete_agent(db: Session, agent_id: int) -> bool:
    agent = db.query(Agent).filter(Agent.id == agent_id).first()
    if agent:
        db.delete(agent)
        db.commit()
        return True
    return False