from datetime import datetime, timedelta, timezone
from services import event_store

def notify_upcoming_events():
    now = datetime.now(timezone.utc)
    for event in event_store.values():
        if now <= event.datetime <= now + timedelta(minutes=5):
            print(f"Upcoming event: {event.name} at {event.datetime.isoformat()}")