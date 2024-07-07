from pydantic import BaseModel

from polyus_nsi.application.nsi.enums import IndustrialStructureTypes


class CreateIndustrialStructureItemRequestDto(BaseModel):
    name: str
    type: IndustrialStructureTypes
    parent_id: int | None = None
