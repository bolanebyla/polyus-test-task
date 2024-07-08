from enum import StrEnum


class IndustrialStructureTypes(StrEnum):
    """
    Типы элементов структуры производства
    """
    # Фабрика
    FACTORY = 'factory'
    # Участок
    DEPARTMENT = 'department'
    # Оборудование
    EQUIPMENT = 'equipment'
