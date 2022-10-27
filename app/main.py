from typing import Union

from fastapi import FastAPI
from app.models.model import Item

app = FastAPI()


@app.get("/")
async def say_hello():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/")
async def create_item(item: Item):
    return item