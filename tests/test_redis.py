import pytest
from src.redis import RedisClient, get_redis_client
from src.config import get_settings


class TestRedisConnection:
    """Test Redis connection and operations using real host values."""

    def test_redis_ping(self):
        """Test that Redis connection is successful."""
        client = get_redis_client()
        assert client.ping() is True

    def test_redis_set_and_get(self):
        """Test setting and getting a key."""
        client = get_redis_client()
        
        # Set a test key
        test_key = "pytest_test_key"
        test_value = "pytest_test_value"
        
        result = client.set(test_key, test_value)
        assert result is True
        
        # Get the key
        retrieved_value = client.get(test_key)
        assert retrieved_value == test_value
        
        # Cleanup
        client.delete(test_key)

    def test_redis_delete(self):
        """Test deleting a key."""
        client = get_redis_client()
        
        test_key = "pytest_delete_key"
        client.set(test_key, "to_be_deleted")
        
        result = client.delete(test_key)
        assert result == 1
        
        # Verify key is gone
        assert client.get(test_key) is None

    def test_redis_exists(self):
        """Test checking if a key exists."""
        client = get_redis_client()
        
        test_key = "pytest_exists_key"
        
        # Key should not exist initially
        assert client.exists(test_key) is False
        
        # Set the key
        client.set(test_key, "exists_value")
        assert client.exists(test_key) is True
        
        # Cleanup
        client.delete(test_key)

    def test_redis_set_with_expiry(self):
        """Test setting a key with expiry."""
        client = get_redis_client()
        
        test_key = "pytest_expiry_key"
        result = client.set(test_key, "expiry_value", expire=60)
        assert result is True
        
        # Key should exist
        assert client.exists(test_key) is True
        
        # Cleanup
        client.delete(test_key)
