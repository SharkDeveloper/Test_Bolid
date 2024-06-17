from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas
from ..database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db() -> Session:
    """
    Предоставить сессию базы данных для внедрения зависимости.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Sensor)
def create_sensor(sensor: schemas.SensorCreate, db: Session = Depends(get_db)) -> schemas.Sensor:
    """
    Создать новый датчик.
    """
    return crud.create_sensor(db=db, sensor=sensor)

@router.get("/{sensor_id}", response_model=schemas.Sensor)
def read_sensor(sensor_id: int, db: Session = Depends(get_db)) -> schemas.Sensor:
    """
    Получить датчик по его ID.
    """
    db_sensor = crud.get_sensor(db, sensor_id=sensor_id)
    if db_sensor is None:
        raise HTTPException(status_code=404, detail="Датчик не найден")
    return db_sensor

@router.get("/", response_model=List[schemas.Sensor])
def read_sensors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> List[schemas.Sensor]:
    """
    Получить список датчиков с пагинацией.
    """
    sensors = crud.get_sensors(db, skip=skip, limit=limit)
    return sensors
