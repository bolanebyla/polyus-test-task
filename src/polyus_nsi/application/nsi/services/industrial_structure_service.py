from typing import List

from attr import frozen

from polyus_nsi.application.nsi.entities.industrial_structure import (
    IndustrialStructureItem,
)
from polyus_nsi.application.nsi.interfaces import IIndustrialStructureRepo


@frozen
class IndustrialStructureService:
    industrial_structure_repo: IIndustrialStructureRepo

    async def get_all_parent_items(
        self,
        item_id: int,
        depth: int,
    ) -> List[IndustrialStructureItem]:
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
        child_items = await self.industrial_structure_repo.get_all_child_items(
            item_id=item_id,
            depth=depth,
        )
        return child_items
