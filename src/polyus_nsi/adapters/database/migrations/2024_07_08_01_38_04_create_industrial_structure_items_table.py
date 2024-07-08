"""create industrial_structure_items table

Revision ID: d1c042970e76
Revises:
Create Date: 2024-07-08 01:38:04.216807+00:00

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy import MetaData
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd1c042970e76'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

metadata = MetaData()

INDUSTRIAL_STRUCTURE_TYPES_ENUM = postgresql.ENUM(
    'FACTORY',
    'DEPARTMENT',
    'EQUIPMENT',
    name='industrial_structure_types',
    metadata=metadata,
    create_type=False,
    validate_strings=True
)


def upgrade() -> None:
    INDUSTRIAL_STRUCTURE_TYPES_ENUM.create(op.get_bind())

    op.create_table(
        'industrial_structure_items',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False, comment='Наименование'),
        sa.Column(
            'type',
            INDUSTRIAL_STRUCTURE_TYPES_ENUM,
            nullable=False,
            comment='Тип',
        ),
        sa.PrimaryKeyConstraint(
            'id', name=op.f('pk_industrial_structure_items')
        )
    )

    op.create_table(
        'industrial_structure_edges',
        sa.Column('previous_item_id', sa.Integer(), nullable=False),
        sa.Column('next_item_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['next_item_id'],
            ['industrial_structure_items.id'],
            name=op.f(
                'fk_industrial_structure_edges_next_item_id_industrial_structure_items'    # noqa
            ),
            ondelete='CASCADE',
        ),
        sa.ForeignKeyConstraint(
            ['previous_item_id'],
            ['industrial_structure_items.id'],
            name=op.f(
                'fk_industrial_structure_edges_previous_item_id_industrial_structure_items'    # noqa
            ),
            ondelete='CASCADE',
        ),
        sa.PrimaryKeyConstraint(
            'previous_item_id',
            'next_item_id',
            name=op.f('pk_industrial_structure_edges'),
        )
    )
    op.create_index(
        op.f('ix_industrial_structure_edges_next_item_id'),
        'industrial_structure_edges',
        ['next_item_id'],
    )


def downgrade() -> None:
    op.drop_index(
        op.f('ix_industrial_structure_edges_next_item_id'),
        table_name='industrial_structure_edges',
    )
    op.drop_table('industrial_structure_edges')
    op.drop_table('industrial_structure_items')
    INDUSTRIAL_STRUCTURE_TYPES_ENUM.drop(op.get_bind())
