from abc import ABC, abstractmethod
from typing import List

from polyus_nsi.application.nsi.dtos.industrial_structure import (
    CreateIndustrialStructureItemRequestDto,
)
from polyus_nsi.application.nsi.entities.industrial_structure import (
    IndustrialStructureItem,
)


class IIndustrialStructureRepo(ABC):
    """
    Репозиторий для работы со структурой производства
    """

    @abstractmethod
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
        ...

    @abstractmethod
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
        ...

    @abstractmethod
    async def create(
        self,
        create_dto: CreateIndustrialStructureItemRequestDto,
    ):
        """
        Создаёт элемент структуры производства
        """
        ...
