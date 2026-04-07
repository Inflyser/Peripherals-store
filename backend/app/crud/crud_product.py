from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


def get_product(db: Session, product_id: int) -> Optional[Product]:
    return db.query(Product).filter(Product.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 100, category: Optional[str] = None) -> List[Product]:
    query = db.query(Product)
    if category:
        query = query.filter(Product.category == category)
    return query.offset(skip).limit(limit).all()


def create_product(db: Session, product: ProductCreate) -> Product:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int, product: ProductUpdate) -> Optional[Product]:
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        update_data = product.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int) -> Optional[Product]:
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product


def search_products(db: Session, query: str, skip: int = 0, limit: int = 100) -> List[Product]:
    return db.query(Product).filter(
        or_(
            Product.name.ilike(f"%{query}%"),
            Product.description.ilike(f"%{query}%"),
            Product.category.ilike(f"%{query}%")
        )
    ).offset(skip).limit(limit).all()
