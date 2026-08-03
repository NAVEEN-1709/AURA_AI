"""
Configuration Loader for AURA AI
"""

from functools import lru_cache
from pathlib import Path

import yaml
from pydantic import BaseModel


# ---------- Configuration Models ----------

class AppSettings(BaseModel):
    name: str
    version: str
    environment: str


class LoggingSettings(BaseModel):
    level: str
    file: str


class LLMSettings(BaseModel):
    default_provider: str
    temperature: float
    max_tokens: int


class SpeechSettings(BaseModel):
    wake_word: str
    language: str


class DatabaseSettings(BaseModel):
    sqlite_path: str


class UISettings(BaseModel):
    theme: str


class Settings(BaseModel):
    app: AppSettings
    logging: LoggingSettings
    llm: LLMSettings
    speech: SpeechSettings
    database: DatabaseSettings
    ui: UISettings


# ---------- Loader ----------

@lru_cache
def get_settings() -> Settings:
    """
    Load settings.yaml and cache the result.
    """
    config_path = Path("config/settings.yaml")

    with config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return Settings(**config)