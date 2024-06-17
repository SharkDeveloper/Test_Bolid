from sqlalchemy.orm import Session
from . import models, schemas
from typing import List, Optional

def get_sensor(db: Session, sensor_id: int) -> Optional[models.Sensor]:
    """
    Получить датчик по его ID.
    """
    return db.query(models.Sensor).filter(models.Sensor.id == sensor_id).first()

def get_sensors(db: Session, skip: int = 0, limit: int = 10) -> List[models.Sensor]:
    """
    Получить список датчиков с пагинацией.
    """
    return db.query(models.Sensor).offset(skip).limit(limit).all()

def create_sensor(db: Session, sensor: schemas.SensorCreate) -> models.Sensor:
    """
    Создать новый датчик.
    """
    db_sensor = models.Sensor(**sensor.dict())
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

def get_event(db: Session, event_id: int) -> Optional[models.Event]:
    """
    Получить событие по его ID.
    """
    return db.query(models.Event).filter(models.Event.id == event_id).first()

def get_events(db: Session, skip: int = 0, limit: int = 10) -> List[models.Event]:
    """
    Получить список событий с пагинацией.
    """
    return db.query(models.Event).offset(skip).limit(limit).all()

def create_event(db: Session, event: schemas.EventCreate) -> models.Event:
    """
    Создать новое событие.
    """
    db_event = models.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_events_by_sensor(db: Session, sensor_id: int) -> List[models.Event]:
    """
    Получить все события для конкретного датчика.
    """
    return db.query(models.Event).filter(models.Event.sensor_id == sensor_id).all()
