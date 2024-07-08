from typing import List

from attr import frozen

from polyus_nsi.application.nsi.dtos.industrial_structure import (
    CreateIndustrialStructureItemRequestDto,
)
from polyus_nsi.application.nsi.entities.industrial_structure import (
    IndustrialStructureItem,
)
from polyus_nsi.application.nsi.interfaces import IIndustrialStructureRepo


@frozen
class IndustrialStructureService:
    """
    Сервис для работы со структурой производства
    """
    industrial_structure_repo: IIndustrialStructureRepo

    async def get_all_parent_items(
        self,
        item_id: int,
        depth: int,
    ) -> List[IndustrialStructureItem]:
        """
        Получает все родительские элементы произвольного уровня

        :param item_id: идентификатор элемента
        для которого нужно вернуть родителей
        :param depth: глубина
        """
        parent_items = await self.industrial_structure_repo.get_all_parent_items( # noqa
            item_id=item_id,
            depth=depth,
        )
        return parent_items

    async def get_all_child_items(
        self,
        item_id: int,
        depth: int,
    ) -> List[IndustrialStructureItem]:
        """
        Получает все дочерние элементы произвольного уровня

        :param item_id: идентификатор элемента
        для которого нужно вернуть потомков
        :param depth: глубина
        """
        child_items = await self.industrial_structure_repo.get_all_child_items(
            item_id=item_id,
            depth=depth,
        )
        return child_items

    async def create_industrial_structure_item(
        self,
        create_dto: CreateIndustrialStructureItemRequestDto,
    ):
        """
        Создаёт элемент структуры производства
        """
        await self.industrial_structure_repo.create(create_dto=create_dto)
