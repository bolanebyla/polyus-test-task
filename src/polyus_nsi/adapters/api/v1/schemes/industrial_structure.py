from pydantic import BaseModel

from polyus_nsi.application.nsi.entities.industrial_structure import (
    IndustrialStructureItem,
)
from polyus_nsi.application.nsi.enums import IndustrialStructureTypes


class IndustrialStructureResponse(BaseModel):
    id: int
    name: str
    type: IndustrialStructureTypes

    @classmethod
    def from_entity(
        cls,
        entity: IndustrialStructureItem,
    ) -> 'IndustrialStructureResponse':
        return cls(
            id=entity.id,
            name=entity.name,
            type=entity.type,
        )
