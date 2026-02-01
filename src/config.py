from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    environment_name: str
    mist_api_key: str
    redis_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()
