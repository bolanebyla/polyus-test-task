import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM

from polyus_nsi.adapters.database.meta import metadata
from polyus_nsi.application.nsi.enums import IndustrialStructureTypes

INDUSTRIAL_STRUCTURE_TYPES_ENUM = ENUM(
    IndustrialStructureTypes,
    name='industrial_structure_types',
    metadata=metadata,
    create_type=False,
    validate_strings=True
)

industrial_structure_items_table = sa.Table(
    'industrial_structure_items',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, nullable=False),
    sa.Column('name', sa.String, nullable=False, comment='Наименование'),
    sa.Column(
        'type',
        INDUSTRIAL_STRUCTURE_TYPES_ENUM,
        nullable=False,
        comment='Тип',
        index=True,
    ),
)
