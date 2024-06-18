from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class Sensor(Base):
    """
    Модель базы данных для датчиков.

    Attributes:
        id (int): Уникальный идентификатор датчика.
        name (str): Название датчика.
        type (int): Тип датчика.
        events (relationship): Связь с моделью событий (Event).
    """
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(Integer)

    events = relationship("Event", back_populates="sensor")

class Event(Base):
    """
    Модель базы данных для событий.

    Attributes:
        id (int): Уникальный идентификатор события.
        sensor_id (int): Идентификатор датчика, к которому привязано событие.
        name (str): Название события.
        temperature (float): Температура, зарегистрированная в событии.
        humidity (float): Влажность, зарегистрированная в событии.
        created_at (datetime): Время создания события.
        sensor (relationship): Связь с моделью датчика (Sensor).
    """
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, ForeignKey('sensors.id'))
    name = Column(String, index=True)
    temperature = Column(Float)
    humidity = Column(Float)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    sensor = relationship("Sensor", back_populates="events")
