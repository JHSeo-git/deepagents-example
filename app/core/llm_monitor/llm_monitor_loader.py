from abc import ABC, abstractmethod

from langfuse.langchain import CallbackHandler

from app.core.config.settings import settings


class LLMMonitor(ABC):
    @abstractmethod
    def get_callback_handler(self) -> CallbackHandler:
        pass


class LLMMonitorLoader:
    _llm_monitor: LLMMonitor | None = None

    def __init__(self):
        self._llm_monitor: LLMMonitor | None = self.get_llm_monitor()

    def get_llm_monitor(self) -> LLMMonitor:
        if settings.LLM_MONITOR == "langfuse":
            from .langfuse import LangfuseMonitor

            if self._llm_monitor is not None:
                return self._llm_monitor

            self._llm_monitor = LangfuseMonitor()
            return self._llm_monitor
        else:
            raise ValueError(f"Unsupported LLM monitor: {settings.LLM_MONITOR}")


_llm_monitor_loader = LLMMonitorLoader()


def get_llm_monitor():
    return _llm_monitor_loader.get_llm_monitor()
