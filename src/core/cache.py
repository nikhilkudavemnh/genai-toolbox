import redis
from typing import Optional, Any
import json
from config import settings

class RedisCache:
    def __init__(self):
        self.redis_client = redis.from_url(settings.redis_url)
    
    async def get(self, key: str) -> Optional[Any]:
        """Get value from cache"""
        try:
            value = self.redis_client.get(key)
            if value:
                return json.loads(value)
        except Exception as e:
            print(f"Cache get error: {e}")
        return None
    
    async def set(self, key: str, value: Any, expire: int = 3600) -> bool:
        """Set value in cache"""
        try:
            self.redis_client.setex(key, expire, json.dumps(value))
            return True
        except Exception as e:
            print(f"Cache set error: {e}")
            return False
    
    async def delete(self, key: str) -> bool:
        """Delete key from cache"""
        try:
            self.redis_client.delete(key)
            return True
        except Exception as e:
            print(f"Cache delete error: {e}")
            return False

cache = RedisCache()