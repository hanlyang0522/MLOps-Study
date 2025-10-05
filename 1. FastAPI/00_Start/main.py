from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")  # HTTP Get 요청의 경로 지정
def read_root():  # Get 요청 처리 함수
    return {"Hello": "World  1123123"}  # JSON 응답 반환. 자동으로 JSON 변환


@app.get("/items/{item_id}")  # items: 경로, {item_id}: 경로 매개변수
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/items/")
# 쿼리 매개변수, 기본값 설정 가능
# URL에서 key-value 쌍으로 전달됨
def read_items(skip=0, limit=10):
    return {"skip": skip, "limit": limit}
