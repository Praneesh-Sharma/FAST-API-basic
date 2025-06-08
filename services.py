from models import Event, EventCreate
from typing import List, Dict, Optional
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

def list_events() -> List[Event]:
    return list(event_store.values())

def get_event(event_id: str) -> Optional[Event]:
    return event_store.get(event_id)