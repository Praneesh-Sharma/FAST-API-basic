# FAST-API-basic

A minimal FastAPI project that allows users to add, list, and fetch events. It also simulates a notification system for events that are about to start within the next 5 minutes.

## Features
- Add new events ('POST /events')
- List all events ('GET /events')
- Retrieve a specific event by ID ('GET /events/{event_id}')
- Notifications (Displayed on terminal every 5 minutes)

## Stack
- Python 3.11+
- Fast API
- APScheduler
- Docker

## File Structure
```
.
├── Dockerfile         # Docker setup to containerize the application
├── README.md          # Project documentation and setup instructions
├── requirements.txt   # Python dependencies
├── main.py            # Entry point for the FastAPI app (routes and server)
├── models.py          # Pydantic models for event data validation
├── services.py        # Logic for managing and storing event data
├── notify.py          # Background job to simulate notifications for upcoming events
├── test.py            # Pytest test cases for all main endpoints
└── .gitignore         # Files and folders to exclude from version control
```

## Getting Started

#### 1. Close the Repository
```bash
git clone https://github.com/Praneesh-Sharma/FAST-API-basic.git
cd FAST-API-basic
```

#### 2.1 Instal Dependencies (Without Docker)
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```
Visit http://localhost:8000/docs

#### 2.2 Running with Docker
```bash
docker build -t event-api .
docker run -p 8000:8000 event-api
```
Visit: http://localhost:8000/docs

####  Running Tests
```bash
pytest test.py
```

#### Notifications
Every 5 minutes, the app checks for any events starting within the next 5 minutes. When such an event is found, it logs the event name and time as a notification in the terminal.


### If I had more time, I would...
- Add storage by integrating a Database
- Add user accounts and authentication
- Implement logging
- Deploy on a cloud platform
- Usage of Background workers
- Implement more features such as modifying or deleting an event

### If this had to serve 10,000 users a day, what would break?
- Data loss risk is the app crashes or restarts
- Latency issues would scale with increase users
- Would need to a set of background workers to handle these mnay users
- Lack of logging means getting the app back up would be difficult in case of a crash.
