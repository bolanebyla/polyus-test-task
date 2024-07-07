from abc import ABC, abstractmethod
from typing import List

from polyus_nsi.application.nsi.entities.industrial_structure import (
    IndustrialStructureItem,
)


class IIndustrialStructureRepo(ABC):

    @abstractmethod
    async def get_all_parent_items(
        self,
        item_id: int,
        depth: int,
    ) -> List[IndustrialStructureItem]:
        ...

    @abstractmethod
    async def get_all_child_items(
        self,
        item_id: int,
        depth: int,
    ) -> List[IndustrialStructureItem]:
        ...
