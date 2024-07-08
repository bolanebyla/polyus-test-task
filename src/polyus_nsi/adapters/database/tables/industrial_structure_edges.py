import sqlalchemy as sa

from polyus_nsi.adapters.database.meta import metadata

industrial_structure_edges_table = sa.Table(
    'industrial_structure_edges',
    metadata,
    sa.Column(
        'previous_item_id',
        sa.Integer,
        sa.ForeignKey(
            'industrial_structure_items.id',
            ondelete='CASCADE',
        ),
        primary_key=True,
        nullable=False,
    ),
    sa.Column(
        'next_item_id',
        sa.Integer,
        sa.ForeignKey(
            'industrial_structure_items.id',
            ondelete='CASCADE',
        ),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)
