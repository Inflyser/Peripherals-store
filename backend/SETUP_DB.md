# Инструкция по настройке базы данных PostgreSQL

## Создание базы данных через pgAdmin

1. Откройте pgAdmin 4
2. Подключитесь к серверу PostgreSQL (обычно localhost, порт 5432)
3. Нажмите правой кнопкой мыши на "Databases" -> "Create" -> "Database..."
4. В поле "Database name" введите: `peripherals_store`
5. Нажмите "Save"

## Настройка подключения

После создания базы данных убедитесь, что файл `.env` содержит правильные данные:

```
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/peripherals_store
```

Замените `YOUR_PASSWORD` на ваш пароль пользователя postgres.

## Запуск миграций

После создания базы данных выполните следующие команды в терминале:

```bash
cd backend
venv\Scripts\activate
alembic upgrade head
```

## Инициализация тестовыми данными

Для добавления тестовых товаров выполните:

```bash
python init_db.py
```

## Запуск сервера

```bash
uvicorn main:app --reload
```

API будет доступно по адресу: http://localhost:8000
Документация API: http://localhost:8000/docs
