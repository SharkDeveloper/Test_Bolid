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

    Yields:
        Session: Сессия базы данных.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)) -> schemas.Event:
    """
    Создать новое событие.

    Args:
        event (schemas.EventCreate): Данные для создания нового события.
        db (Session, optional): Сессия базы данных. По умолчанию создается новая сессия.

    Returns:
        schemas.Event: Созданный объект события.
    """
    return crud.create_event(db=db, event=event)

@router.get("/{event_id}", response_model=schemas.Event)
def read_event(event_id: int, db: Session = Depends(get_db)) -> schemas.Event:
    """
    Получить событие по его ID.

    Args:
        event_id (int): ID события.
        db (Session, optional): Сессия базы данных. По умолчанию создается новая сессия.

    Returns:
        schemas.Event: Объект события.

    Raises:
        HTTPException: Если событие с указанным ID не найдено.
    """
    db_event = crud.get_event(db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Событие не найдено")
    return db_event

@router.get("/", response_model=List[schemas.Event])
def read_events(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> List[schemas.Event]:
    """
    Получить список событий с пагинацией.

    Args:
        skip (int, optional): Количество пропускаемых записей. По умолчанию 0.
        limit (int, optional): Максимальное количество возвращаемых записей. По умолчанию 10.
        db (Session, optional): Сессия базы данных. По умолчанию создается новая сессия.

    Returns:
        List[schemas.Event]: Список объектов событий.
    """
    events = crud.get_events(db, skip=skip, limit=limit)
    return events

@router.get("/sensor/{sensor_id}", response_model=List[schemas.Event])
def read_events_by_sensor(sensor_id: int, db: Session = Depends(get_db)) -> List[schemas.Event]:
    """
    Получить все события для конкретного датчика.

    Args:
        sensor_id (int): ID датчика.
        db (Session, optional): Сессия базы данных. По умолчанию создается новая сессия.

    Returns:
        List[schemas.Event]: Список объектов событий, связанных с указанным датчиком.
    """
    events = crud.get_events_by_sensor(db, sensor_id=sensor_id)
    return events
