"""create ix for type in industrial_structure_items table

Revision ID: c0b839ff9f28
Revises: d1c042970e76
Create Date: 2024-07-08 05:54:05.014929+00:00

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'c0b839ff9f28'
down_revision: Union[str, None] = 'd1c042970e76'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index(
        op.f('ix_industrial_structure_items_type'),
        'industrial_structure_items',
        ['type'],
    )


def downgrade() -> None:
    op.drop_index(
        op.f('ix_industrial_structure_items_type'),
        table_name='industrial_structure_items',
    )
