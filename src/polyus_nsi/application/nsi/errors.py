from polyus_nsi.application.base.errors import AppError


class IndustrialStructureItemByIdNotFound(AppError):
    code = 'nsi.industrial_structure_item_by_id_not_found'
    message_template = 'Структура производства с id {id_} не найдена'
