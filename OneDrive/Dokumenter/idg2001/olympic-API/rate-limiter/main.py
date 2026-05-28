from fastapi import FastAPI
from datetime import datetime, timedelta

app = FastAPI()

requests_data = {}


@app.get("/")
def root():
    return {"message": "Rate Limiter running"}


@app.post("/{user_id}")
def add_request(user_id: int):
    now = datetime.now()

    if user_id not in requests_data:
        requests_data[user_id] = []

    requests_data[user_id].append(now)

    requests_data[user_id] = [
        t for t in requests_data[user_id]
        if now - t < timedelta(seconds=10)
    ]

    return {"message": "Request registered"}


@app.get("/{user_id}")
def get_requests(user_id: int):
    now = datetime.now()

    if user_id not in requests_data:
        return {
            "requests": 0,
            "delay": 0
        }

    requests_data[user_id] = [
        t for t in requests_data[user_id]
        if now - t < timedelta(seconds=10)
    ]

    request_count = len(requests_data[user_id])

    delay = 0

    if request_count > 10:
        delay = (request_count - 10) / 10

    return {
        "requests": request_count,
        "delay": delay
    }