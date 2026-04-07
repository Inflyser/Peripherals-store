# Peripherals Store Frontend

Frontend для магазина игровой периферии на Vue.js + TypeScript.

## Установка

1. Установите зависимости:
```bash
npm install
```

## Запуск

Запустите сервер разработки:
```bash
npm run dev
```

Приложение будет доступно по адресу: http://localhost:5173

## Сборка

Для сборки продакшн версии:
```bash
npm run build
```

## Структура проекта

- `src/components` - Vue компоненты
- `src/views` - Страницы приложения
- `src/router` - Vue Router конфигурация
- `src/stores` - Pinia хранилища состояния
- `src/api` - API клиенты
- `src/types` - TypeScript типы
- `src/assets` - Статические ресурсы

## Компоненты

- `ProductCard` - Карточка товара
- `ProductList` - Список товаров
- `SearchBar` - Строка поиска
- `CategoryFilter` - Фильтр по категориям

## Страницы

- `HomeView` - Главная страница с каталогом товаров
- `ProductView` - Страница отдельного товара
