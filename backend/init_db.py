"""
Скрипт для инициализации базы данных с тестовыми данными
"""
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models.product import Product

# Создаем таблицы
Base.metadata.create_all(bind=engine)

# Тестовые данные
test_products = [
    {
        "name": "Logitech G Pro X Superlight",
        "description": "Легчайшая беспроводная игровая мышь для профессиональных геймеров. Вес всего 63 грамма, сенсор HERO 25K с точностью 25600 DPI.",
        "price": 12999.00,
        "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500",
        "category": "Мышки",
        "stock": 15
    },
    {
        "name": "Razer BlackWidow V3 Pro",
        "description": "Беспроводная механическая клавиатура с RGB подсветкой и переключателями Razer Green. Время работы до 200 часов.",
        "price": 18999.00,
        "image_url": "https://images.unsplash.com/photo-1587829741301-dc798b91add1?w=500",
        "category": "Клавиатуры",
        "stock": 8
    },
    {
        "name": "SteelSeries Arctis Pro Wireless",
        "description": "Премиальные беспроводные игровые наушники с Hi-Fi аудио, двойной беспроводной связью и RGB подсветкой.",
        "price": 24999.00,
        "image_url": "https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?w=500",
        "category": "Наушники",
        "stock": 5
    },
    {
        "name": "HyperX Alloy Origins Core",
        "description": "Компактная механическая клавиатура с переключателями HyperX Red и алюминиевым корпусом.",
        "price": 8999.00,
        "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500",
        "category": "Клавиатуры",
        "stock": 12
    },
    {
        "name": "ASUS ROG Gladius III",
        "description": "Игровая мышь с оптическими переключателями, сенсором ROG 19000 DPI и RGB подсветкой.",
        "price": 9999.00,
        "image_url": "https://images.unsplash.com/photo-1527814050087-3793815479db?w=500",
        "category": "Мышки",
        "stock": 20
    },
    {
        "name": "Corsair K95 RGB Platinum",
        "description": "Флагманская механическая клавиатура с переключателями Cherry MX Speed, 6 макро-клавишами и RGB подсветкой.",
        "price": 21999.00,
        "image_url": "https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?w=500",
        "category": "Клавиатуры",
        "stock": 3
    },
    {
        "name": "Logitech G933 Artemis Spectrum",
        "description": "Беспроводные игровые наушники с 7.1 Surround звуком, RGB подсветкой и временем работы до 12 часов.",
        "price": 15999.00,
        "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500",
        "category": "Наушники",
        "stock": 7
    },
    {
        "name": "Razer DeathAdder V2",
        "description": "Эргономичная игровая мышь с оптическим сенсором 20000 DPI и переключателями Razer Optical.",
        "price": 7999.00,
        "image_url": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=500",
        "category": "Мышки",
        "stock": 25
    },
    {
        "name": "SteelSeries Apex Pro TKL",
        "description": "Механическая клавиатура с регулируемыми переключателями OmniPoint и OLED дисплеем.",
        "price": 16999.00,
        "image_url": "https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=500",
        "category": "Клавиатуры",
        "stock": 6
    },
    {
        "name": "HyperX Cloud II",
        "description": "Проводные игровые наушники с виртуальным 7.1 Surround звуком и алюминиевым корпусом.",
        "price": 6999.00,
        "image_url": "https://images.unsplash.com/photo-1484704849700-f032a568e944?w=500",
        "category": "Наушники",
        "stock": 30
    },
    {
        "name": "Logitech G502 HERO",
        "description": "Легендарная игровая мышь с сенсором HERO 25K, 11 программируемыми кнопками и системой балансировки.",
        "price": 6499.00,
        "image_url": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=500",
        "category": "Мышки",
        "stock": 18
    },
    {
        "name": "Razer Kraken Ultimate",
        "description": "Игровые наушники с THX Spatial Audio, RGB подсветкой и охлаждающими гелевыми подушками.",
        "price": 11999.00,
        "image_url": "https://images.unsplash.com/photo-1613040809024-b4ef7ba99bc3?w=500",
        "category": "Наушники",
        "stock": 10
    }
]


def init_db():
    db: Session = SessionLocal()
    try:
        # Проверяем, есть ли уже товары
        existing_products = db.query(Product).count()
        if existing_products > 0:
            print(f"База данных уже содержит {existing_products} товаров. Пропускаем инициализацию.")
            return

        # Добавляем тестовые данные
        for product_data in test_products:
            product = Product(**product_data)
            db.add(product)
        
        db.commit()
        print(f"Успешно добавлено {len(test_products)} товаров в базу данных!")
        
    except Exception as e:
        db.rollback()
        print(f"Ошибка при инициализации базы данных: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    init_db()
