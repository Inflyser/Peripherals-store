# Peripherals Store Backend

Backend для магазина игровой периферии на FastAPI.

## Установка

1. Создайте виртуальное окружение:
```bash
python -m venv venv
```

2. Активируйте виртуальное окружение:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Настройка базы данных

1. Установите PostgreSQL и создайте базу данных:
```sql
CREATE DATABASE peripherals_store;
```

2. Настройте подключение в файле `.env`:
```
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/peripherals_store
```

3. Запустите миграции:
```bash
alembic upgrade head
```

## Запуск

Запустите сервер:
```bash
uvicorn main:app --reload
```

API будет доступен по адресу: http://localhost:8000

Документация API: http://localhost:8000/docs

## API Endpoints

### Products

- `GET /products` - Получить список товаров
- `GET /products/search?q=query` - Поиск товаров
- `GET /products/{id}` - Получить товар по ID
- `POST /products` - Создать новый товар
- `PUT /products/{id}` - Обновить товар
- `DELETE /products/{id}` - Удалить товар
