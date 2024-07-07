import attr


@attr.dataclass
class IndustrialStructureItem:
    title: str
    id: int | None = None
