from fastapi import FastAPI
from models import Event, EventCreate
from services import add_event, list_events
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