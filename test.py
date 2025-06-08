from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_post_event():
    response = client.post("/events", json={
        "name": "Test Event",
        "datetime": "2025-06-08T16:20:28.264000Z"
    })
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    
def test_get_events():
    response = client.get("/events")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0  # Assuming at least one event was created in the previous test
    
def test_get_event_by_id():
    post_response = client.post("/events", json={
        "name": "New Event",
        "datetime": "2023-10-01T10:00:00Z"
    })
    event_id = post_response.json()["id"]
    
    response = client.get(f"/events/{event_id}".format(event_id=event_id)) 
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "{}".format(event_id)

def test_get_event_by_id_not_found():
    response = client.get("/events/12345678-1234-5678-1234-567812345678")
    assert response.status_code == 404
    assert response.json() == {"detail": "Event not found"}