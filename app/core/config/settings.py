import os

from pydantic_settings import BaseSettings, SettingsConfigDict

env = os.getenv("ENV", "local")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=[f".env.{env}", ".env"],
        env_ignore_empty=True,
        extra="ignore",
    )
    ENV: str = "local"

    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    AWS_MODEL_ID: str

    LLM_MONITOR: str = "langfuse"
    LANGFUSE_PUBLIC_KEY: str
    LANGFUSE_SECRET_KEY: str
    LANGFUSE_HOST: str

    TAVILY_API_KEY: str


settings = Settings()
