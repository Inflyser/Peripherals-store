# Peripherals Store

Магазин игровой периферии с современным стеком технологий.

## Стек технологий
https://img.mvideo.ru/Big/30093442bb.jpg?width=600&fmt=avif
### Backend
- **FastAPI** - Современный веб-фреймворк для Python
- **SQLAlchemy** - ORM для работы с базой данных
- **Alembic** - Инструмент для миграций базы данных
- **PostgreSQL** - Реляционная база данных
- **Pydantic** - Валидация данных

### Frontend
- **Vue.js 3** - Прогрессивный JavaScript фреймворк
- **TypeScript** - Статическая типизация
- **Vite** - Сборщик модулей
- **Vue Router** - Маршрутизация
- **Pinia** - Управление состоянием
- **Axios** - HTTP клиент

## Структура проекта

```
peripherals-store/
├── backend/              # Backend на FastAPI
│   ├── app/
│   │   ├── models/      # SQLAlchemy модели
│   │   ├── schemas/     # Pydantic схемы
│   │   ├── routers/     # API роутеры
│   │   ├── crud/        # CRUD операции
│   │   └── database/    # Настройка БД
│   ├── alembic/         # Миграции
│   └── main.py          # Точка входа
└── frontend/            # Frontend на Vue.js
    └── src/
        ├── components/  # Vue компоненты
        ├── views/       # Страницы
        ├── router/      # Vue Router
        ├── stores/      # Pinia хранилища
        ├── api/         # API клиенты
        └── types/       # TypeScript типы
```

## Установка и запуск

### Требования
- Python 3.10+
- Node.js 18+
- PostgreSQL 14+

### Backend

1. Перейдите в директорию backend:
```bash
cd backend
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
```

3. Активируйте виртуальное окружение:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

5. Создайте базу данных через pgAdmin:
   - Откройте pgAdmin 4
   - Подключитесь к серверу PostgreSQL (localhost:5432)
   - Нажмите правой кнопкой на "Databases" -> "Create" -> "Database..."
   - В поле "Database name" введите: `peripherals_store`
   - Нажмите "Save"

6. Настройте подключение в файле `.env`:
```
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/peripherals_store
```
Замените `your_password` на ваш пароль пользователя postgres.

7. Запустите миграции:
```bash
alembic upgrade head
```

8. Добавьте тестовые данные:
```bash
python init_db.py
```

9. Запустите сервер:
```bash
uvicorn main:app --reload
```

API будет доступно по адресу: http://localhost:8000

Документация API: http://localhost:8000/docs

### Запуск через Docker

Для быстрого запуска всех сервисов через Docker:

```bash
docker-compose up --build
```

Приложение будет доступно:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API документация: http://localhost:8000/docs

Подробнее см. [`DOCKER.md`](DOCKER.md)

### Frontend

1. Откройте новый терминал и перейдите в директорию frontend:
```bash
cd frontend
```

2. Установите зависимости:
```bash
npm install
```

3. Запустите сервер разработки:
```bash
npm run dev
```

Приложение будет доступно по адресу: http://localhost:5173

## API Endpoints

### Products

- `GET /products` - Получить список товаров
- `GET /products/search?q=query` - Поиск товаров
- `GET /products/{id}` - Получить товар по ID
- `POST /products` - Создать новый товар
- `PUT /products/{id}` - Обновить товар
- `DELETE /products/{id}` - Удалить товар

## Возможности

- ✅ Каталог товаров с карточками
- ✅ Поиск товаров по названию, описанию и категории
- ✅ Фильтрация по категориям
- ✅ Страница отдельного товара
- ✅ Отображение наличия на складе
- ✅ Адаптивный дизайн
- ✅ CORS настройка для фронтенда

## Планы на будущее

- 🛒 Корзина покупок
- 👤 Авторизация пользователей
- 📦 Управление заказами
- ⭐ Отзывы и рейтинги
- 🎨 Темная тема
- 📱 PWA поддержка

## Лицензия

MIT
