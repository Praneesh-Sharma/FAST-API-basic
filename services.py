from models import Event, EventCreate
from typing import List, Dict
from uuid import uuid4

event_store: Dict[str, Event] = {}

def add_event(event_create: EventCreate) -> Event:
    event_id = str(uuid4())
    event = Event(
        id=event_id,
        name=event_create.name,
        datetime=event_create.datetime
    )
    event_store[event_id] = event
    return event