import sourcedefender
from datetime import date, datetime
from fastapi import FastAPI
from routers import routMrepSasData
from apikey import apiKey
import  uvicorn

# API Key Import
# from fastapi import Security, Depends, FastAPI, HTTPException
# from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
# from fastapi.openapi.docs import get_swagger_ui_html
# from fastapi.openapi.utils import get_openapi
# from starlette.status import HTTP_403_FORBIDDEN
# from starlette.responses import RedirectResponse, JSONResponse

app=FastAPI()
app.include_router(routMrepSasData.router)

# # app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
# app=FastAPI()

# @app.get("/")
# async def homepage():
#     return "Welcome to the security test!"


# @app.get("/logout")
# async def route_logout_and_remove_cookie():
#     response = RedirectResponse(url="/")
#     response.delete_cookie(apiKey.API_KEY_NAME, domain=apiKey.COOKIE_DOMAIN)
#     return response


# @app.get("/openapi.json", tags=["documentation"])
# async def get_open_api_endpoint(api_key: APIKey = Depends(apiKey.get_api_key)):
#     response = JSONResponse(
#         get_openapi(title="FastAPI security test", version=1, routes=app.routes)
#     )
#     return response


# @app.get("/documentation", tags=["documentation"])
# async def get_documentation(api_key: APIKey = Depends(apiKey.get_api_key)):
#     response = get_swagger_ui_html(openapi_url="/openapi.json", title="docs")
#     response.set_cookie(
#         apiKey.API_KEY_NAME,
#         value=api_key,
#         domain=apiKey.COOKIE_DOMAIN,
#         httponly=True,
#         max_age=1800,
#         expires=1800,
#     )
#     return response

# @app.get("/secure_endpoint", tags=["test"])
# async def get_open_api_endpoint(api_key: APIKey = Depends(apiKey.get_api_key)):
#     response = "How cool is this?"
#     return response


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=9000)
