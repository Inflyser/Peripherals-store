from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import products_router

app = FastAPI(
    title="Peripherals Store API",
    description="API для магазина игровой периферии",
    version="0.1.0"
)

# Настройка CORS для фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(products_router)


@app.get("/")
def read_root():
    return {"message": "Peripherals Store API", "version": "0.1.0"}

@app.get("/api")
def read_api_root():
    return {"message": "Peripherals Store API", "version": "0.1.0"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
