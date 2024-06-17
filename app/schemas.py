from pydantic import BaseModel
from typing import List, Optional

class SensorBase(BaseModel):
    """
    Базовая схема для датчика.
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
    """
    id: int

    class Config:
        orm_mode = True

class EventBase(BaseModel):
    """
    Базовая схема для события.
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
    """
    id: int
    created_at: Optional[str]

    class Config:
        orm_mode = True
