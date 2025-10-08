from fastapi import FastAPI

app = FastAPI()


# get은 url의 쿼리 string에 데이터를 담아 전송
# get은 주로 데이터를 조회할 때 사용 --> body는 공백
# 누구나 접근 가능
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


# post는 body에 데이터를 담아 전송
# url에는 데이터 드러나지 않음
@app.post("/items/")
def create_item(item: dict):
    return {"item": item}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "updated_item": item}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} has been deleted"}
