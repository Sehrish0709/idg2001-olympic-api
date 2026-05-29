from fastapi import FastAPI
from datetime import datetime, timedelta
import csv
import os

app = FastAPI()

logs = []
retention_days = 7


@app.get("/")
def root():
    return {"message": "Logger service running"}


@app.post("/log")
def add_log(data: dict):
    logs.append(data)

    # Delete old log files
    for file in os.listdir("logs"):
        filepath = os.path.join("logs", file)

        if os.path.isfile(filepath):
            file_time = datetime.fromtimestamp(
                os.path.getmtime(filepath)
            )

            if datetime.now() - file_time > timedelta(days=retention_days):
                os.remove(filepath)

    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"logs/log_{today}.csv"

    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "time",
                "username",
                "endpoint",
                "tokens"
            ])

        writer.writerow([
            datetime.now().isoformat(),
            data.get("username", ""),
            data.get("endpoint", ""),
            data.get("tokens", 0)
        ])

    return {"message": "Log added"}


@app.get("/retention")
def get_retention():
    return {"n": retention_days}


@app.post("/retention")
def set_retention(data: dict):
    global retention_days

    retention_days = data["n"]

    return {"n": retention_days}
