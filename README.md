# Interview Project

## Setup

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload


## How to run

### Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

### Frontend
Open frontend/index.html in browser

## Structure
- backend/ – FastAPI server
- frontend/ – simple UI
