# Установка базового образа
FROM python:3.11.7


# Установка переменных окружения
ENV SRC_DIR=/app \
    APP_USER=backend-user \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    GUNICORN_PROCESSES=4 \
    GUNICORN_CONNECTIONS=8 \
    GUNICORN_LOGLEVEL='error' \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PATH="/app/.venv/bin:$PATH"

# Установка рабочего каталога
WORKDIR /app

# Установка Poetry
RUN pip install poetry

# Копирование файлов проекта
COPY . .

# Установка зависимостей проекта
RUN poetry install --no-dev

# Установка Supervisor
RUN apt-get update && apt-get install -y supervisor \
    && rm -rf /var/lib/apt/lists/*

# Копирование конфигурационного файла supervisord
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Применение Django операций при запуске контейнера
# Используем ENTRYPOINT, чтобы сначала выполнить миграции, а затем запустить supervisord
ENTRYPOINT ["bash", "-c", "\
    poetry run python manage.py makemigrations && \
    poetry run python manage.py migrate && \
    poetry run python manage.py loaddata db.json && \
    poetry run python manage.py collectstatic --noinput && \
    /usr/bin/supervisord -n"]
