from fastapi import FastAPI

from parser.src.swagger_parser import SwaggerParser

app = FastAPI()

swagger_parser = SwaggerParser()

@app.get("/parse-swagger")
def parseSwagger(swagger_json: str):
    return swagger_parser.parse_swagger_into_documentation(swagger_json)