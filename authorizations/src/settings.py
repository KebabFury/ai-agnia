from pydantic_settings import BaseSettings


class BaseHackathonSettings(BaseSettings):
    user_token_from_tg_bot: str = "7884940461:AAHeRLMuv8Kbn2eXfdGusxhd-CwPeNrXckg"
    save_auth_data_endpoint: str = "https://aes-agniachallenge-case.olymp.innopolis.university/save-authorization-data"


class TodoistAuthSettings(BaseSettings):
    todoist_oauth_api_url: str = "https://todoist.com/oauth/authorize/"
    todoist_token_exchange_api_url: str = "https://todoist.com/oauth/access_token/"
    todoist_redirect_url: str = "http://localhost:9000"
    todoist_client_id: str = "c2778732236a4499bf8d3aa9d18f78a2"
    todoist_scope: str = "task:add,data:read,data:read_write,data:delete"
    todoist_state: str = "some_secret_state"
    todoist_client_secret: str = "d7be3872056e4bbab047abf9f316e583"

class CoreServiceSettings(BaseSettings):
    base_api_url: str = "http://91.197.98.50:5243"
    todoist_authorize_url: str = "todoist/authorize"
    todoist_get_token_url: str = "todoist/get-token"
    list_docs_url: str = "provider/list-docs"


base_hackathon_settings = BaseHackathonSettings()
todoist_auth_settings = TodoistAuthSettings()
core_service_settings = CoreServiceSettings()
