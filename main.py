from fastapi import FastAPI, HTTPException
from models import Event, EventCreate
from services import add_event, list_events, get_event
from typing import List

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/events", response_model=Event)
def create_event(event: EventCreate):
    return add_event(event)

@app.get("/events", response_model=List[Event])
def get_events():
    return list_events()

@app.get("/events/{event_id}", response_model=Event)
def fetch_event(event_id: str):
    event = get_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event