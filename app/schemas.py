from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SensorBase(BaseModel):
    """
    Базовая схема для датчика.

    Attributes:
        name (str): Название датчика.
        type (int): Тип датчика.
    """
    name: str
    type: int

class SensorCreate(SensorBase):
    """
    Схема для создания датчика.
    """
    pass

class Sensor(SensorBase):
    """
    Схема для отображения датчика.

    Attributes:
        id (int): Уникальный идентификатор датчика.
    """
    id: int

    class Config:
        orm_mode = True

class EventBase(BaseModel):
    """
    Базовая схема для события.

    Attributes:
        sensor_id (int): Идентификатор датчика, к которому привязано событие.
        name (str): Название события.
        temperature (float): Температура, зарегистрированная в событии.
        humidity (float): Влажность, зарегистрированная в событии.
    """
    sensor_id: int
    name: str
    temperature: float
    humidity: float

class EventCreate(EventBase):
    """
    Схема для создания события.
    """
    pass

class Event(EventBase):
    """
    Схема для отображения события.

    Attributes:
        id (int): Уникальный идентификатор события.
        created_at (Optional[datetime]): Время создания события.
    """
    id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
