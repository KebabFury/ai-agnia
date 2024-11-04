import os

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    team_id: str = "a698e896-231a-4299-94e6-a000a634f6c6"
    backend_api: str = "https://aes-agniachallenge-case.olymp.innopolis.university"
    root_directory: str = os.path.dirname(__file__)

class CoreServiceSettings(BaseSettings):
    base_api_url: str = "http://91.197.98.50:5243"
    todoist_authorize_url: str = "todoist/authorize"
    todoist_get_token_url: str = "todoist/get-token"
    list_docs_url: str = "provider/list-docs"

settings = Settings()
core_service_settings = CoreServiceSettings()
