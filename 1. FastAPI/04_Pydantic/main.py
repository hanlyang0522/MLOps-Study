from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()


class Item(BaseModel):
    name: str = Field(..., title="Item Name", min_length=2, max_length=50)
    description: str = Field(
        None, description="The description of the item", max_length=300
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tag: List[str] = Field(default=[], alias="item-tags")


class Item2(BaseModel):
    # '...'는 이 필드가 기본값 없이 반드시 필요함을 의미합니다.
    # gt=0: 0보다 커야 함
    item_id: int = Field(
        ..., gt=0, title="Item ID", description="The unique identifier of the item."
    )

    # min_length, max_length: 문자열 길이 제한
    name: str = Field(..., min_length=3, max_length=50)

    # alias: 외부 데이터에서는 'item-price'라는 이름으로 들어올 수 있음을 의미
    price: float = Field(..., gt=0, alias="item-price")

    # 기본값이 0.0이고, 0 이상이어야 함
    tax: Optional[float] = Field(0.0, ge=0)


class NestedItem(BaseModel):
    id: int
    name: str
    item: Item  # 중첩 클래스 가능


@app.post("/items/")
async def create_item(item: Item):
    return {"item": item.model_dump()}


@app.post("/items2/")
async def create_item2(item: Item2):
    return {"item": item.model_dump()}
