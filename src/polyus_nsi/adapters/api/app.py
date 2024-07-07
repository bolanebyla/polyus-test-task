from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from polyus_nsi.adapters.api.exception_handlers import app_error_handler
from polyus_nsi.adapters.api.routers import root_router
from polyus_nsi.application.base.errors import AppError

app = FastAPI(
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )
    ]
)
app.include_router(root_router)

app.add_exception_handler(AppError, app_error_handler)
