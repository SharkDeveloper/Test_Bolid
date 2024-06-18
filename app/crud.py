from sqlalchemy.orm import Session
from . import models, schemas
from typing import List, Optional

def get_sensor(db: Session, sensor_id: int) -> Optional[models.Sensor]:
    """
    Получить датчик по его ID.

    Args:
        db (Session): Сессия базы данных.
        sensor_id (int): ID датчика.

    Returns:
        Optional[models.Sensor]: Объект датчика, если найден, иначе None.
    """
    return db.query(models.Sensor).filter(models.Sensor.id == sensor_id).first()

def get_sensors(db: Session, skip: int = 0, limit: int = 10) -> List[models.Sensor]:
    """
    Получить список датчиков с пагинацией.

    Args:
        db (Session): Сессия базы данных.
        skip (int, optional): Количество пропускаемых записей. По умолчанию 0.
        limit (int, optional): Максимальное количество возвращаемых записей. По умолчанию 10.

    Returns:
        List[models.Sensor]: Список объектов датчиков.
    """
    return db.query(models.Sensor).offset(skip).limit(limit).all()

def create_sensor(db: Session, sensor: schemas.SensorCreate) -> models.Sensor:
    """
    Создать новый датчик.

    Args:
        db (Session): Сессия базы данных.
        sensor (schemas.SensorCreate): Данные для создания нового датчика.

    Returns:
        models.Sensor: Созданный объект датчика.
    """
    db_sensor = models.Sensor(**sensor.dict())
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

def get_event(db: Session, event_id: int) -> Optional[models.Event]:
    """
    Получить событие по его ID.

    Args:
        db (Session): Сессия базы данных.
        event_id (int): ID события.

    Returns:
        Optional[models.Event]: Объект события, если найден, иначе None.
    """
    return db.query(models.Event).filter(models.Event.id == event_id).first()

def get_events(db: Session, skip: int = 0, limit: int = 10) -> List[models.Event]:
    """
    Получить список событий с пагинацией.

    Args:
        db (Session): Сессия базы данных.
        skip (int, optional): Количество пропускаемых записей. По умолчанию 0.
        limit (int, optional): Максимальное количество возвращаемых записей. По умолчанию 10.

    Returns:
        List[models.Event]: Список объектов событий.
    """
    return db.query(models.Event).offset(skip).limit(limit).all()

def create_event(db: Session, event: schemas.EventCreate) -> models.Event:
    """
    Создать новое событие.

    Args:
        db (Session): Сессия базы данных.
        event (schemas.EventCreate): Данные для создания нового события.

    Returns:
        models.Event: Созданный объект события.
    """
    db_event = models.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_events_by_sensor(db: Session, sensor_id: int) -> List[models.Event]:
    """
    Получить все события для конкретного датчика.

    Args:
        db (Session): Сессия базы данных.
        sensor_id (int): ID датчика.

    Returns:
        List[models.Event]: Список объектов событий, связанных с указанным датчиком.
    """
    return db.query(models.Event).filter(models.Event.sensor_id == sensor_id).all()
