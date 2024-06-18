import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_sensor():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/sensors/", json={"name": "Sensor1"})
        assert response.status_code == 200
        assert response.json()["name"] == "Sensor1"

@pytest.mark.asyncio
async def test_get_sensors():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/sensors/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_event():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/events/", json={"sensor_id": 1, "temperature": 25.5, "created_at": "2023-06-18T10:10:18.955535"})
        assert response.status_code == 200
        assert response.json()["temperature"] == 25.5

@pytest.mark.asyncio
async def test_get_events():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/events/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_update_event():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.put("/events/1", json={"sensor_id": 1, "temperature": 30.0, "created_at": "2023-06-18T10:10:18.955535"})
        assert response.status_code == 200
        assert response.json()["temperature"] == 30.0

@pytest.mark.asyncio
async def test_delete_event():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/events/1")
        assert response.status_code == 200
        assert response.json()["message"] == "Event deleted"
