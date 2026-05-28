from fastapi import FastAPI
from .database import engine, Base
from .routes import user, tokens, olympics

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/v2")
app.include_router(tokens.router, prefix="/v2")
app.include_router(olympics.router, prefix="/v2")


@app.get("/")
def root():
    return {"message": "Olympic API running"}