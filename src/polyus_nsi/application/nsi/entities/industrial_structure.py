import attr

from polyus_nsi.application.nsi.enums import IndustrialStructureTypes


@attr.dataclass
class IndustrialStructureItem:
    title: str
    type: IndustrialStructureTypes
    id: int | None = None
