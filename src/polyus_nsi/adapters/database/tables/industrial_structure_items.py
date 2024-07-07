import sqlalchemy as sa

from polyus_nsi.adapters.database.meta import metadata

industrial_structure_items_table = sa.Table(
    'industrial_structure_items',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, nullable=False),
    sa.Column('name', sa.String, nullable=False, comment='Наименование'),
)
