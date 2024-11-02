
from pydantic_settings import BaseSettings


class LlmModelSettings(BaseSettings):
    get_response_url: str = "https://aes-agniachallenge-case.olymp.innopolis.university/llm/get-response"
    model_name = "meta-llama/Llama-3.2-11B-Vision-Instruct"


llm_model_settings = LlmModelSettings()