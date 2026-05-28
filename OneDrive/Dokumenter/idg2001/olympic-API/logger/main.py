from fastapi import FastAPI

app = FastAPI()

logs = []
retention_days = 7


@app.get("/")
def root():
    return {"message": "Logger service running"}


@app.post("/log")
def add_log(data: dict):
    logs.append(data)

    return {"message": "Log added"}


@app.get("/retention")
def get_retention():
    return {"n": retention_days}


@app.post("/retention")
def set_retention(data: dict):
    global retention_days

    retention_days = data["n"]

    return {"n": retention_days}