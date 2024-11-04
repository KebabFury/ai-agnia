from fastapi import FastAPI

from authorizations.src.settings import base_hackathon_settings, core_service_settings
import requests

app = FastAPI()

assert (
    base_hackathon_settings.user_token_from_tg_bot != ""
), "Укажите Telegram токен в settings.py"

@app.get("/todoist/authorize")
def authorize_in_todoist():
    core_authorize_endpoint_url = f"{core_service_settings.base_api_url}/{core_service_settings.todoist_authorize_url}"
    response = requests.get(core_authorize_endpoint_url)
    return response.json()

@app.get("/todoist/get-token")
def get_todoist_token(
    code: str = None,
    state: str = None,
    error: str = None,
):
    core_get_token_url = f"{core_service_settings.base_api_url}/{core_service_settings.todoist_get_token_url}"
    query_params = []
    if code is not None:
        query_params.append(f"code={code}")
    if state is not None:
        query_params.append(f"state={state}")
    if error is not None:
        query_params.append(f"error={error}")

    if query_params:
        core_get_token_url += "?" + "&".join(query_params)
    response = requests.get(core_get_token_url)
    print(response.json())
    print(response.content)
    return response.json()

@app.get("/{system_name}/authorize")
def authorize_in_custom_system(system_name: str):
    core_authorize_endpoint_url = f"{core_service_settings.base_api_url}/provider/{system_name}/authorize"
    response = requests.get(core_authorize_endpoint_url)
    print(response.json())
    return response.json()

@app.get("/{system_name}/get-token")
def get_token_for_custom_system(system_name: str, code: str = None, error: str = None):
    core_get_token_endpoint_url = f"{core_service_settings.base_api_url}/provider/{system_name}/get-token"
    query_params = []
    if code is not None:
        query_params.append(f"code={code}")
    if error is not None:
        query_params.append(f"error={error}")

    if query_params:
        core_get_token_endpoint_url += "?" + "&".join(query_params)
    response = requests.get(core_get_token_endpoint_url)
    print(response.json())
    return response.json()


@app.get("/list-docs")
def list_docs():
    list_docs_url = f"{core_service_settings.base_api_url}/{core_service_settings.list_docs_url}"
    print(list_docs_url)
    response = requests.get(list_docs_url)
    return response.json()

@app.get("/create-files")
def create_files():
    list_docs_url = f"{core_service_settings.base_api_url}/{core_service_settings.list_docs_url}"
    response = requests.get(list_docs_url)
    data = response.json()

    

# @app.get("/todoist/authorize")
# def authorize_in_todoist():
#     return {"url": todoist.authorize()}


# @app.get("/todoist/get-token", include_in_schema=False)
# def get_todoist_token(
#     code: str = None,
#     state: str = None,
#     error: str = None,
# ):
#     if error == "invalid_application_status":
#         raise HTTPException(status_code=500, detail="Invalid application status")
#     elif error == "invalid_scope":
#         raise HTTPException(status_code=400, detail="Invalid scope")
#     elif error == "access_denied":
#         raise HTTPException(status_code=403, detail="User denied authorization")

#     authorization_token = todoist.callback(code, state, error)
#     return save_authorization_data_and_return_response(
#         authorization_token, system_name="Todoist"
#     )
