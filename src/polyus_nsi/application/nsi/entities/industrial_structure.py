import attr

from polyus_nsi.application.nsi.enums import IndustrialStructureTypes


@attr.dataclass
class IndustrialStructureItem:
    """
    Элемент структуры производства
    """
    name: str
    type: IndustrialStructureTypes
    id: int | None = None
