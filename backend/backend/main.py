# import subprocess
import random
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from functools import lru_cache
from .data.config import CreateConnection
from sqlalchemy.orm import Session

connection = CreateConnection()
base = connection.get_base




def get_db() -> Session:
    db = connection.get_SessionLocal
    try:
        yield db
    finally:
        db.close()

from .routers import route_1

app = FastAPI()
app.include_router(route_1.router, prefix='/results')

@app.get('/healthcheck', status_code=200)
def health():
    status_code = ["I'm live!!", "What are you looking??"]
    return JSONResponse(random.choice(status_code), 200)