from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class EventCreate(BaseModel):
    name: str
    datetime: datetime

class Event(BaseModel):
    id: UUID