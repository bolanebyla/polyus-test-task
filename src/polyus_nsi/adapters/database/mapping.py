from sqlalchemy.orm import registry

from polyus_nsi.adapters.database.tables import industrial_structure_items_table
from polyus_nsi.application.nsi.entities.industrial_structure import (
    IndustrialStructureItem,
)

mapper = registry()

mapper.map_imperatively(
    IndustrialStructureItem,
    industrial_structure_items_table,
)
