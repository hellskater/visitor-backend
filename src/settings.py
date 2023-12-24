import os
from typing import Any

from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from pydantic import Field
from pydantic.types import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class _Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env"))
    SECRET_KEY: SecretStr = Field(
        default="b24843116d84a46f8b28433f1c22b526d0f393a14f28fc2c7868f793b468eae0"
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    MONGO_URI: str = os.getenv(key="MONGO_URI", default="mongodb://localhost:27017")

    TELESIGN_CUSTOMER_ID: str = os.getenv(key="TELESIGN_CUSTOMER_ID", default="")
    TELESIGN_API_KEY: str = os.getenv(key="TELESIGN_API_KEY", default="")


# Make this a singleton to avoid reloading it from the env everytime
SETTINGS = _Settings()

MotorClient: Any = AsyncIOMotorClient(SETTINGS.MONGO_URI)
Engine = AIOEngine(client=MotorClient, database="visitor")
