# Этап сборки
FROM node:18-alpine AS builder

WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем остальной код
COPY . .

# Собираем приложение
RUN npm run build:vite

# Этап production с nginx
FROM nginx:alpine

# Копируем собранные файлы из этапа builder
COPY --from=builder /app/dist /usr/share/nginx/html

# Копируем конфигурацию nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Экспортируем порт
EXPOSE 5173

# Запускаем nginx
CMD ["nginx", "-g", "daemon off;"]
