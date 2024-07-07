from fastapi import APIRouter

from polyus_nsi.adapters.api.v1 import controllers

v1_router = APIRouter(prefix='/v1')

v1_router.include_router(controllers.nsi_router, tags=['NSI'])
