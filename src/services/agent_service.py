from typing import List, Optional
from core.cache import cache
from core.logging import logger

class AgentService:
    def __init__(self):
        self.cache_prefix = "agent:"
    
    async def get_agent_from_cache(self, agent_id: int) -> Optional[dict]:
        """Get agent from cache"""
        cache_key = f"{self.cache_prefix}{agent_id}"
        return await cache.get(cache_key)
    
    async def cache_agent(self, agent_id: int, agent_data: dict) -> bool:
        """Cache agent data"""
        cache_key = f"{self.cache_prefix}{agent_id}"
        return await cache.set(cache_key, agent_data, expire=1800)  # 30 minutes
    
    async def execute_agent(self, agent_id: int) -> dict:
        """Execute agent logic"""
        logger.info(f"Executing agent {agent_id}")
        
        # Check cache first
        cached_result = await self.get_agent_from_cache(agent_id)
        if cached_result:
            logger.info(f"Agent {agent_id} result found in cache")
            return cached_result
        
        # Execute agent logic here
        result = {
            "agent_id": agent_id,
            "status": "executed",
            "result": "Agent execution completed"
        }
        
        # Cache the result
        await self.cache_agent(agent_id, result)
        
        return result

agent_service = AgentService()