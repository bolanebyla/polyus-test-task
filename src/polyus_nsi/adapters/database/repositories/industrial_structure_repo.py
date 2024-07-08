from typing import List

from attr import frozen
from sqlalchemy import insert, literal, select

from polyus_nsi.adapters.database.tables import industrial_structure_edges_table
from polyus_nsi.application.nsi.dtos.industrial_structure import (
    CreateIndustrialStructureItemRequestDto,
)
from polyus_nsi.application.nsi.entities.industrial_structure import (
    IndustrialStructureItem,
)
from polyus_nsi.application.nsi.interfaces import IIndustrialStructureRepo

from .base import AsyncBaseRepo


@frozen
class IndustrialStructureRepo(IIndustrialStructureRepo, AsyncBaseRepo):

    async def _get_all_parent_or_child_items(
        self,
        item_id: int,
        depth: int,
        parent: bool,
    ) -> List[IndustrialStructureItem]:
        edges_alias = industrial_structure_edges_table.alias()

        top_q = select(
            edges_alias.c.previous_item_id, edges_alias.c.next_item_id,
            literal(1).label('depth')
        )

        if parent:
            top_q = top_q.where(edges_alias.c.next_item_id == item_id)
        else:
            top_q = top_q.where(edges_alias.c.previous_item_id == item_id)

        top_q = top_q.cte('al_tree', recursive=True)

        top_q_alias = top_q.alias()

        bottom_q = select(
            edges_alias.c.previous_item_id, edges_alias.c.next_item_id,
            top_q_alias.c.depth + 1
        )

        if parent:
            bottom_q = bottom_q.where(
                edges_alias.c.next_item_id == top_q_alias.c.previous_item_id
            )
        else:
            bottom_q = bottom_q.where(
                edges_alias.c.previous_item_id == top_q_alias.c.next_item_id
            )

        rec_q = top_q.union(bottom_q)

        q = select(IndustrialStructureItem, ).where(rec_q.c.depth == depth)

        if parent:
            q = q.select_from(
                rec_q.join(
                    IndustrialStructureItem,
                    rec_q.c.previous_item_id == IndustrialStructureItem.id,
                )
            )
        else:
            q = q.select_from(
                rec_q.join(
                    IndustrialStructureItem,
                    rec_q.c.next_item_id == IndustrialStructureItem.id,
                )
            )

        result = await self.session.scalars(q)
        return result.all()    # noqa

    async def get_all_parent_items(
        self,
        item_id: int,
        depth: int,
    ) -> List[IndustrialStructureItem]:
        parent_items = await self._get_all_parent_or_child_items(
            item_id=item_id,
            depth=depth,
            parent=True,
        )
        return parent_items

    async def get_all_child_items(
        self,
        item_id: int,
        depth: int,
    ) -> List[IndustrialStructureItem]:
        child_items = await self._get_all_parent_or_child_items(
            item_id=item_id,
            depth=depth,
            parent=False,
        )
        return child_items

    async def create(
        self,
        create_dto: CreateIndustrialStructureItemRequestDto,
    ):
        result = await self.session.scalars(
            insert(IndustrialStructureItem).returning(IndustrialStructureItem),
            {
                'name': create_dto.name,
            }
        )
        item = result.one()

        if create_dto.parent_id is not None:
            await self.session.execute(
                insert(industrial_structure_edges_table), {
                    'previous_item_id': create_dto.parent_id,
                    'next_item_id': item.id
                }
            )
