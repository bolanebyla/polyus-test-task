import sqlalchemy as sa

from polyus_nsi.adapters.database.meta import metadata

industrial_structure_edges_table = sa.Table(
    'industrial_structure_edges', metadata,
    sa.Column(
        'previous_industrial_structure_item_id',
        sa.Integer,
        primary_key=True,
        nullable=False,
    ),
    sa.Column(
        'next_industrial_structure_item_id',
        sa.Integer,
        primary_key=True,
        nullable=False,
    ),
    sa.PrimaryKeyConstraint(
        'previous_industrial_structure_item_id',
        'next_industrial_structure_item_id',
    )
)
