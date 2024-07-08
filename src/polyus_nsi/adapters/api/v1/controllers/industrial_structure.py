from typing import Annotated, List

from fastapi import APIRouter, Depends

from polyus_nsi.adapters.api.factories import (
    create_industrial_structure_service,
)
from polyus_nsi.adapters.api.v1.schemes.industrial_structure import (
    IndustrialStructureResponse,
)
from polyus_nsi.application.nsi.dtos.industrial_structure import (
    CreateIndustrialStructureItemRequestDto,
)
from polyus_nsi.application.nsi.enums import IndustrialStructureTypes
from polyus_nsi.application.nsi.services import IndustrialStructureService

industrial_structure_router = APIRouter(prefix='/industrial_structure')


@industrial_structure_router.get(
    '/get_all_parent_items',
    summary='Получить все родительские элементы произвольного уровня'
)
async def get_all_parent_items(
    item_id: int,
    depth: int,
    industrial_structure_service: Annotated[
        IndustrialStructureService,
        Depends(create_industrial_structure_service)],
) -> List[IndustrialStructureResponse]:
    parent_items = await industrial_structure_service.get_all_parent_items(
        item_id=item_id,
        depth=depth,
    )
    return [
        IndustrialStructureResponse.from_entity(item) for item in parent_items
    ]


@industrial_structure_router.get(
    '/get_all_child_items',
    summary='Получить все дочерние элементы произвольного уровня'
)
async def get_all_child_items(
    item_id: int,
    depth: int,
    industrial_structure_service: Annotated[
        IndustrialStructureService,
        Depends(create_industrial_structure_service)],
) -> List[IndustrialStructureResponse]:
    child_items = await industrial_structure_service.get_all_child_items(
        item_id=item_id,
        depth=depth,
    )
    return [
        IndustrialStructureResponse.from_entity(item) for item in child_items
    ]


@industrial_structure_router.post(
    '/create', summary='Создать элемент структуры производства'
)
async def create(
    create_request: CreateIndustrialStructureItemRequestDto,
    industrial_structure_service: Annotated[
        IndustrialStructureService,
        Depends(create_industrial_structure_service)],
) -> IndustrialStructureResponse:
    item = await industrial_structure_service.create_industrial_structure_item(
        create_request
    )
    return IndustrialStructureResponse.from_entity(item)


@industrial_structure_router.get(
    '/get_by_id', summary='Получить запись по идентификатору'
)
async def get_by_id(
    item_id: int,
    industrial_structure_service: Annotated[
        IndustrialStructureService,
        Depends(create_industrial_structure_service)],
) -> IndustrialStructureResponse:
    item = await industrial_structure_service.get_by_id(id_=item_id, )
    return IndustrialStructureResponse.from_entity(item)


@industrial_structure_router.get(
    '/get_all_by_type',
    summary='Получить список элементов структуры производства по типу',
)
async def get_all_by_type(
    industrial_structure_type: IndustrialStructureTypes,
    industrial_structure_service: Annotated[
        IndustrialStructureService,
        Depends(create_industrial_structure_service)],
) -> List[IndustrialStructureResponse]:
    items = await industrial_structure_service.get_all_by_type(
        industrial_structure_type=industrial_structure_type,
    )
    return [IndustrialStructureResponse.from_entity(item) for item in items]
