from fastapi import FastAPI, Query
from typing import List, Dict

app = FastAPI()


# type hinting
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {
        "item_id": item_id,
    }


@app.get("/getdata/")
def read_items(data: str = "funcoding"):
    return {"data": data}


@app.get("/items/")
# list type hint는 반드시 Query와 함께 사용
# url 입력 예시: /?q=1&q=2&q=3 -> q=[1,2,3]
async def read_items(q: List[int] = Query([])):
    return {"q": q}


@app.post("/create-item/")
async def create_item(item: Dict[str, int]):
    return item


@app.get("/querytest/")
# list, dict, tuple, set 등 다중 사용 가능
def query_test(q: List[Dict[int, str]] = Query([])):
    return {"q": q}
