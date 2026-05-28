from fastapi import FastAPI
import uuid
app = FastAPI()
codes = {}


@app.get("/")
def root():
    return {"message": "Token Shop is running"}


@app.post("/buy")
def buy_tokens(data: dict):
    secret = str(uuid.uuid4())

    codes[secret] = {
        "money": data["money"],
        "used": False
    }

    return {"secret": secret}


@app.post("/validate")
def validate_code(data: dict):
    code = data["code"]

    if code not in codes:
        return {"error": "Invalid code"}

    if codes[code]["used"]:
        return {"error": "Code already used"}

    codes[code]["used"] = True

    return {
        "tokens": codes[code]["money"]
    }