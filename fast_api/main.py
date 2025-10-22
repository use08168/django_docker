from fastapi import FastAPI

from path_parmas import router as path_params_router
from query_params import router as query_params_router
from request_body import router as request_body_router

app = FastAPI()

app.include_router(router=path_params_router)
app.include_router(router=query_params_router)
app.include_router(router=request_body_router)