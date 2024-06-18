import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app  # импортируем FastAPI приложение
from app.database import Base
from app.routers.events import get_db
from app.models import Sensor, Event
from app.schemas import SensorCreate, EventCreate



client = TestClient(app)


# Тесты для сенсоров
@pytest.mark.asyncio
async def test_create_sensor():
    response = client.post("/sensors/", json={"name": "Sensor1", "type": 0})
    assert response.status_code == 200
    assert response.json()["name"] == "Sensor1"

@pytest.mark.asyncio
async def test_read_sensor():
    response = client.get("/sensors/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Sensor1"

@pytest.mark.asyncio
async def test_read_sensors():
    response = client.get("/sensors/?skip=0&limit=10")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

# Тесты для событий
@pytest.mark.asyncio
async def test_create_event():
    # Создадим датчик для привязки события
    response = client.post("/events/", json={"sensor_id": 1, "temperature": 20.0, "name" : "Пошел дождь", "humidity": 100})
    assert response.status_code == 200
    assert response.json()["temperature"] == 20.0

@pytest.mark.asyncio
async def test_read_event():
    response = client.get("/events/1")
    assert response.status_code == 200
    assert response.json()["temperature"] == 20.0

@pytest.mark.asyncio
async def test_read_events():
    response = client.get("/events/?skip=0&limit=10")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

@pytest.mark.asyncio
async def test_read_events_by_sensor():
    response = client.get("/events/sensor/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
