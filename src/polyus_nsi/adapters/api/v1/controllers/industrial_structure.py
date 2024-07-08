from typing import Annotated

from fastapi import APIRouter, Depends

from polyus_nsi.adapters.api.factories import (
    create_industrial_structure_service,
)
from polyus_nsi.application.nsi.dtos.industrial_structure import (
    CreateIndustrialStructureItemRequestDto,
)
from polyus_nsi.application.nsi.services import IndustrialStructureService

industrial_structure_router = APIRouter(prefix='/industrial_structure')


@industrial_structure_router.get('/get_all_parent_items')
async def get_all_parent_items(
    item_id: int,
    depth: int,
    industrial_structure_service: Annotated[
        IndustrialStructureService,
        Depends(create_industrial_structure_service)],
):
    parent_items = await industrial_structure_service.get_all_parent_items(
        item_id=item_id,
        depth=depth,
    )
    return parent_items


@industrial_structure_router.get('/get_all_child_items')
async def get_all_child_items(
    item_id: int,
    depth: int,
    industrial_structure_service: Annotated[
        IndustrialStructureService,
        Depends(create_industrial_structure_service)],
):
    child_items = await industrial_structure_service.get_all_child_items(
        item_id=item_id,
        depth=depth,
    )
    return child_items


@industrial_structure_router.post('/create')
async def create(
    create_request: CreateIndustrialStructureItemRequestDto,
    industrial_structure_service: Annotated[
        IndustrialStructureService,
        Depends(create_industrial_structure_service)],
):
    await industrial_structure_service.create_industrial_structure_item(
        create_request
    )
