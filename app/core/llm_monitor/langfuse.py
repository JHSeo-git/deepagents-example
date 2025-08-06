from langfuse import Langfuse
from langfuse.langchain import CallbackHandler

from app.core.config.settings import settings
from app.utils.logging import get_logger

from .llm_monitor_loader import LLMMonitor

logger = get_logger(__name__)


class LangfuseMonitor(LLMMonitor):
    _langfuse: Langfuse | None = None

    def __init__(self):
        self._langfuse: Langfuse | None = self._get_instance()

    def _get_instance(self) -> Langfuse:
        if self._langfuse is not None:
            return self._langfuse

        self._langfuse = Langfuse(
            public_key=settings.LANGFUSE_PUBLIC_KEY,
            secret_key=settings.LANGFUSE_SECRET_KEY,
            host=settings.LANGFUSE_HOST,
            environment=settings.ENV,
        )

        # Verify connection
        if self._langfuse.auth_check():
            logger.info("Langfuse client is authenticated and ready!")
        else:
            logger.error(
                "Authentication failed. Please check your credentials and host."
            )

        return self._langfuse

    def get_callback_handler(self) -> CallbackHandler:
        return CallbackHandler()
