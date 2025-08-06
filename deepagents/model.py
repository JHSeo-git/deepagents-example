from langchain_aws import ChatBedrock


def get_default_model():
    return ChatBedrock(model_name="claude-sonnet-4-20250514", max_tokens=64000)
