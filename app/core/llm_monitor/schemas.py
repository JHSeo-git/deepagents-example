from enum import Enum


class TraceTags(Enum):
    LLM_CHAIN = "llm_chain"
    AGENT = "agent"
    RAG = "rag"
