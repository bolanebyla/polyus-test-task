# Тестовое задание Полюс

Реализовано api для работы со справочником "Структура производства": 
- "Фабрика"
- "Участки"
- "Оборудование"

Функционал: 
- создание элемента справочника
- получение всех родительских элементов произвольного уровня для выбранной записи
- получение всех дочерних элементов произвольного уровня для выбранной записи
- получение записи справочника по идентификатору
- получение записей справочника по типу ("Фабрика", "Участки", "Оборудование")

## Зависимости
- PostgreSQL
- [poetry](https://python-poetry.org/)

## Запуск проекта

### Переменные окружения
- **DB_URL** - подключение к БД (пример: `postgresql+asyncpg://polyus-test-task:polyus-test-task@localhost:8500/polyus-test-task`)

### Сборка
```shell
poetry build --format wheel
```

### Установка проекта как пакета
```shell
pip install dist/*.whl
```

### Применение миграций

```shell
python -m polyus_nsi.run.alembic_runner upgrade head
```
*alembic_runner это обертка, аргументы просто проксируются в cli alembic
```shell
python -m polyus_nsi.run.alembic_runner <other args>
```

### Запуск API
#### uvicorn
```shell
uvicorn polyus_nsi.run.polyus_nsi_api:app --host=0.0.0.0 --port=8000
```

#### python
```shell
python -m polyus_nsi.run.polyus_nsi_api.py
```

## Запуск проекта для разработки
*при необходимости развернуть БД в docker-compose
```shell
docker-compose -f .\deployment\docker-compose.local.yaml up -d --build
```
Установить зависимости
```shell
poetry install
```

Каталог `src/` является корневым для python модулей проекта, 
например в IDE можно его пометить как sources_root
(в случае запуска из консоли, нужно определить `PYTHONPATH` и сослать на этот каталог)

Запустить необходимые компоненты из `src/polyus_nsi/run/`

### Развертывание в контейнере
Изучить Dockerfile в каталоге развертывания (`deployment/`), собрать контейнер с необходимой командой запуска (выбрать нужный entrypoint.sh)

### Развертывание в docker-compose
Использовать `docker-compose.yaml` в корне проекта
```shell
docker-compose up -d --build
```
Включает в себя:
- postgreSQL 16
- применение миграций
- запуск api (http://127.0.0.1:8000/docs)


### Openapi документация
- Файл документации доступен по адресу http://127.0.0.1:8000/openapi.json
- Swagger доступен по адресу http://127.0.0.1:8000/docs