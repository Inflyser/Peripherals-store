from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.schemas.product import Product, ProductCreate, ProductUpdate
from app.crud import crud_product

router = APIRouter(prefix="/products", tags=["products"], redirect_slashes=False)


@router.get("/", response_model=List[Product])
def read_products(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    category: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Получить список товаров с пагинацией и фильтрацией по категории"""
    products = crud_product.get_products(db, skip=skip, limit=limit, category=category)
    return products


@router.get("/search", response_model=List[Product])
def search_products(
    q: str = Query(..., min_length=1),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Поиск товаров по названию, описанию или категории"""
    products = crud_product.search_products(db, query=q, skip=skip, limit=limit)
    return products


@router.get("/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    """Получить товар по ID"""
    product = crud_product.get_product(db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    return product


@router.post("/", response_model=Product, status_code=201)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """Создать новый товар"""
    return crud_product.create_product(db=db, product=product)


@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    """Обновить товар"""
    db_product = crud_product.update_product(db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    return db_product


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """Удалить товар"""
    db_product = crud_product.delete_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    return None
