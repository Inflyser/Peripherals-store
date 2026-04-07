#!/bin/sh

# Ждем, пока PostgreSQL будет готов
echo "Waiting for PostgreSQL..."
while ! pg_isready -U postgres -h postgres -p 5432 > /dev/null 2>&1; do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

echo "PostgreSQL is up - executing command"

# Применяем миграции Alembic
echo "Running migrations..."
alembic upgrade head

# Инициализируем тестовые данные
echo "Initializing database with sample data..."
python init_db.py

# Запускаем приложение
echo "Starting FastAPI server..."
exec uvicorn main:app --host 0.0.0.0 --port 8000
