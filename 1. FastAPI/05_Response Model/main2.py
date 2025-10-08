from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Cat(BaseModel):
    name: str


class Dog(BaseModel):
    name: str


class Item(BaseModel):
    name: str


# union은 여러개 중 하나만 맞으면 됨
@app.get("/animal/", response_model=Union[Cat, Dog])
async def get_animal(animal: str):
    if animal == "cat":
        return Cat(name="Whiskers")
    else:
        return Dog(name="Fido")


# list는 모두 맞아야 함
@app.get("/items/", response_model=List[Item])
async def get_items():
    return [{"name": "Item 1"}, {"name": "Item 2"}]
