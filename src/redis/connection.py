import redis
from typing import Optional
from src.config import settings

class RedisConnection:
    _instance: Optional[redis.Redis] = None
    
    @classmethod
    def get_instance(cls) -> redis.Redis:
        if cls._instance is None:
            cls._instance = redis.from_url(
                settings.redis_url,
                decode_responses=True,
                health_check_interval=30
            )
        return cls._instance
    
    @classmethod
    def close_connection(cls):
        if cls._instance:
            cls._instance.close()
            cls._instance = None

def get_redis() -> redis.Redis:
    return RedisConnection.get_instance()