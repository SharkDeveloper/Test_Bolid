import json
from sqlalchemy.orm import Session
from . import models, schemas, crud

def load_events_from_json(db: Session, filename: str) -> None:
    """
    Загрузить события из JSON файла и сохранить их в базе данных.

    Args:
        db (Session): Сессия базы данных.
        filename (str): относительный путь до JSON файла с событиями.
    """
    with open(filename, 'r') as f:
        events = json.load(f)
        for event in events:
            sensor_id = event.get('sensor_id')
            sensor = crud.get_sensor(db, sensor_id=sensor_id)
            if not sensor:
                print(f'Датчик с ID {sensor_id} не существует')
                continue
            event_data = schemas.EventCreate(
                sensor_id=sensor_id,
                name=event['name'],
                temperature=event['temperature'],
                humidity=event['humidity']
            )
            crud.create_event(db, event=event_data)
