from fastapi import Request
from starlette.responses import JSONResponse

from polyus_nsi.application.base.errors import AppError


def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={
            'message': exc.message,
            'code': exc.code,
        },
    )
