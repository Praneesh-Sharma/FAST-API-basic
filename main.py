from fastapi import FastAPI
from models import Event, EventCreate
from services import add_event

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/events", response_model=Event)
def create_event(event: EventCreate):
    return add_event(event)