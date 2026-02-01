import redis
from src.config import get_settings


class RedisClient:
    def __init__(self):
        settings = get_settings()
        url = settings.redis_url
        self.client = redis.Redis.from_url(url, decode_responses=True)

    def set(self, key: str, value: str, expire: int = None) -> bool:
        """Set a key-value pair in Redis."""
        return self.client.setex(key, expire, value) if expire else self.client.set(key, value)

    def get(self, key: str) -> str | None:
        """Get a value by key from Redis."""
        return self.client.get(key)

    def delete(self, key: str) -> int:
        """Delete a key from Redis."""
        return self.client.delete(key)

    def ping(self) -> bool:
        """Test Redis connection."""
        try:
            return self.client.ping()
        except redis.ConnectionError:
            return False


def get_redis_client() -> RedisClient:
    """Get a Redis client instance."""
    return RedisClient()
