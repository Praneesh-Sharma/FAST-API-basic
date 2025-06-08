from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from services import event_store

def notify_upcoming_events():
    now = datetime.now(ZoneInfo("Europe/Brussels"))
    for event in event_store.values():
        if now <= event.datetime <= now + timedelta(minutes=5):
            print(f"Upcoming event: {event.name} at {event.datetime.isoformat()}")