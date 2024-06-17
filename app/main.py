from fastapi import FastAPI
from .routers import sensors, events

app = FastAPI()

app.include_router(sensors.router, prefix="/sensors", tags=["sensors"])
app.include_router(events.router, prefix="/events", tags=["events"])

@app.get("/")
def read_root() -> dict:
    """
    Корневой эндпоинт для проверки работоспособности API.
    """
    return {"message": "Добро пожаловать в Bolid API"}
