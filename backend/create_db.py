"""
Скрипт для создания базы данных PostgreSQL
"""
import psycopg2
from psycopg2 import OperationalError

def create_database():
    """Создает базу данных peripherals_store"""
    try:
        # Подключаемся к PostgreSQL (к базе postgres по умолчанию)
        connection = psycopg2.connect(
            host='localhost',
            port=5432,
            user='postgres',
            password='',  # Пустой пароль
            database='postgres'
        )
        connection.autocommit = True
        cursor = connection.cursor()

        # Проверяем, существует ли база данных
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'peripherals_store'")
        exists = cursor.fetchone()

        if not exists:
            cursor.execute("CREATE DATABASE peripherals_store")
            print("База данных 'peripherals_store' успешно создана!")
        else:
            print("База данных 'peripherals_store' уже существует.")

        cursor.close()
        connection.close()

    except OperationalError as e:
        print(f"Ошибка подключения к PostgreSQL: {e}")
        print("\nВозможные решения:")
        print("1. Проверьте, запущен ли PostgreSQL сервер")
        print("2. Проверьте настройки аутентификации в pg_hba.conf")
        print("3. Создайте базу данных вручную через pgAdmin")
        return False

    return True


if __name__ == "__main__":
    create_database()
