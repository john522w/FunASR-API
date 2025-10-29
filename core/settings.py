import os
from functools import lru_cache
from typing import Literal, ClassVar
from pydantic import model_validator
from pydantic_settings import SettingsConfigDict,BaseSettings
from .path_conf import BASE_PATH

class Settings(BaseSettings):

    model_config: ClassVar = SettingsConfigDict(
        env_file=f"{BASE_PATH}/.env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True,
    )

    ENVIRONMENT: Literal["dev", "pro"] = "dev"

    LOG_DIR: str = f"{BASE_PATH}/logs"
    LOG_LEVEL: str = "INFO"
    UPLOAD_DIR: str = f"{BASE_PATH}/uploads"


    @model_validator(mode="before")
    def validate_env(cls, values):
        env = values.get("ENVIRONMENT", "dev")
        env_file_map = {
            "dev": f"{BASE_PATH}/.env.dev",
            "pro": f"{BASE_PATH}/.env.pro",
        }
        values["env_file"] = env_file_map.get(env, f"{BASE_PATH}/.env.dev")
        return values

@lru_cache()
def get_settings() -> Settings:
    return Settings()