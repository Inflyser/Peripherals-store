# Запуск проекта через Docker

## Требования
- Docker
- Docker Compose

## Быстрый запуск

1. Запустите все сервисы:
```bash
docker-compose up --build
```

2. Приложение будет доступно:
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API документация: http://localhost:8000/docs

## Полная остановка

```bash
docker-compose down
```

## Остановка с удалением volumes

```bash
docker-compose down -v
```

## Пересборка контейнеров

```bash
docker-compose up --build --force-recreate
```

## Просмотр логов

```bash
# Все сервисы
docker-compose logs

# Только backend
docker-compose logs backend

# Только frontend
docker-compose logs frontend

# Только postgres
docker-compose logs postgres
```

## Структура сервисов

- **postgres**: PostgreSQL база данных (порт 5432)
- **backend**: FastAPI приложение (порт 8000)
- **frontend**: Vue.js приложение (порт 5173)

## Примечания

- База данных автоматически инициализируется тестовыми данными при запуске
- Миграции Alembic применяются автоматически
- Данные базы данных сохраняются в Docker volume `postgres_data`
