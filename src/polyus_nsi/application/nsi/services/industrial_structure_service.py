from typing import List

from attr import frozen

from polyus_nsi.application.nsi.dtos.industrial_structure import (
    CreateIndustrialStructureItemRequestDto,
)
from polyus_nsi.application.nsi.entities.industrial_structure import (
    IndustrialStructureItem,
)
from polyus_nsi.application.nsi.enums import IndustrialStructureTypes
from polyus_nsi.application.nsi.errors import (
    IndustrialStructureItemByIdNotFound,
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
    ) -> IndustrialStructureItem:
        """
        Создаёт элемент структуры производства
        """
        return await self.industrial_structure_repo.create(
            create_dto=create_dto
        )

    async def get_by_id(self, id_) -> IndustrialStructureItem:
        """
        Получает запись по идентификатору

        :exception IndustrialStructureItemByIdNotFound
        """
        item = await self.industrial_structure_repo.get_by_id(id_=id_)

        if item is None:
            raise IndustrialStructureItemByIdNotFound(id_=id_)
        return item

    async def get_all_by_type(
        self, industrial_structure_type: IndustrialStructureTypes
    ) -> List[IndustrialStructureItem]:
        """
        Получает список элементов структуры производства по типу
        """
        items = await self.industrial_structure_repo.get_all_by_type(
            industrial_structure_type=industrial_structure_type
        )
        return items
