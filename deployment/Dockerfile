# Стадия сборки
FROM python:3.11.8-slim as build
# Глобальные переменные стадии сборки
ENV USERNAME=app
ENV PIP_CONFIG_FILE=/app/pip.conf

# Установка бинарных пакетов
RUN apt update \
    && apt install -y unixodbc-dev
# Копирование кода
COPY ./src /app/src
COPY pyproject.toml poetry.lock app/

WORKDIR /app

# Установка зависимостей python
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry build --format wheel
RUN pip install dist/*.whl
# Смена пользователя
RUN groupadd -r $USERNAME &&\
    useradd -r -g $USERNAME -d /home/$USERNAME -s /sbin/nologin -c "Docker image user" app
# Копирование скриптов запуска
COPY --chown=app:app ./deployment/entrypoints/entrypoint*.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/entrypoint*.sh
# Определение стартовой директории и пользователя
WORKDIR /usr/local/lib/python3.11/site-packages/    build: ./Dockerfile

USER $USERNAME

# Перетегирование основного образа
FROM build as final