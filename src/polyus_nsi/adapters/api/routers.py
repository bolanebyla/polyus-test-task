from fastapi import APIRouter

from polyus_nsi.adapters.api.v1.routers import v1_router

root_router = APIRouter(prefix='/api')
root_router.include_router(v1_router)
