from typing import List

from attr import frozen
from sqlalchemy import literal, select

from polyus_nsi.adapters.database.tables import industrial_structure_edges_table
from polyus_nsi.application.nsi.entities.industrial_structure import (
    IndustrialStructureItem,
)
from polyus_nsi.application.nsi.interfaces import IIndustrialStructureRepo

from .base import AsyncBaseRepo


@frozen
class IndustrialStructureRepo(IIndustrialStructureRepo, AsyncBaseRepo):

    async def get_all_parent_items(
        self,
        item_id: int,
        depth: int,
    ) -> List[IndustrialStructureItem]:
        top_q = select(
            industrial_structure_edges_table.c.
            previous_industrial_structure_item_id,
            industrial_structure_edges_table.c.
            next_industrial_structure_item_id,
            literal(1).label('depth')
        ).where(
            industrial_structure_edges_table.c.next_industrial_structure_item_id
            == item_id
        ).cte(
            'al_tree', recursive=True
        )

        top_q_alias = top_q.alias()

        # yapf: disable
        bottom_q = select(
            industrial_structure_edges_table.c.
            previous_industrial_structure_item_id,
            industrial_structure_edges_table.c.
            next_industrial_structure_item_id, top_q_alias.c.depth + 1
        ).where(
            industrial_structure_edges_table.c.next_industrial_structure_item_id == top_q_alias.c.previous_industrial_structure_item_id    # noqa
        )
        # yapf: enable

        recursive_q = top_q.union(bottom_q)

        # yapf: disable
        q = select(
            IndustrialStructureItem,
        ).select_from(
            recursive_q.join(
                IndustrialStructureItem,
                recursive_q.c.previous_industrial_structure_item_id == IndustrialStructureItem.id,    # noqa
            )
        ).where(recursive_q.c.depth == depth)
        # yapf: enable

        result = await self.session.scalars(q)
        return result.all()

    async def get_all_child_items(
        self,
        item_id: int,
        depth: int,
    ) -> List[IndustrialStructureItem]:
        top_q = select(
            industrial_structure_edges_table.c.
            previous_industrial_structure_item_id,
            industrial_structure_edges_table.c.
            next_industrial_structure_item_id,
            literal(1).label('depth')
        ).where(
            industrial_structure_edges_table.c.
            previous_industrial_structure_item_id == item_id
        ).cte(
            'al_tree', recursive=True
        )

        top_q_alias = top_q.alias()

        # yapf: disable
        bottom_q = select(
            industrial_structure_edges_table.c.
            previous_industrial_structure_item_id,
            industrial_structure_edges_table.c.
            next_industrial_structure_item_id, top_q_alias.c.depth + 1
        ).where(
            industrial_structure_edges_table.c.previous_industrial_structure_item_id == top_q_alias.c.next_industrial_structure_item_id    # noqa
        )
        # yapf: enable

        recursive_q = top_q.union(bottom_q)

        # yapf: disable
        q = select(
            IndustrialStructureItem,
        ).select_from(
            recursive_q.join(
                IndustrialStructureItem,
                recursive_q.c.next_industrial_structure_item_id == IndustrialStructureItem.id,    # noqa
            )
        ).where(recursive_q.c.depth == depth)
        # yapf: enable

        result = await self.session.scalars(q)
        return result.all()
