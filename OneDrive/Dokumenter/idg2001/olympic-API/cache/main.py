from fastapi import FastAPI
from datetime import datetime, timedelta

app = FastAPI()

cache = {}

hits = 0
misses = 0


@app.get("/")
def root():
    return {"message": "Cache service running"}


@app.get("/log")
def get_log():
    return {
        "hits": hits,
        "misses": misses
    }


@app.get("/cache/{key}")
def get_cache(key: str):
    global hits, misses

    if key in cache:
        timestamp = cache[key]["time"]

        if datetime.now() - timestamp < timedelta(minutes=1):
            hits += 1
            return cache[key]["data"]

        del cache[key]

    misses += 1
    return {"error": "Not found"}


@app.post("/cache/{key}")
def set_cache(key: str, data: dict):
    cache[key] = {
        "data": data,
        "time": datetime.now()
    }

    return {"message": "Cached"}
