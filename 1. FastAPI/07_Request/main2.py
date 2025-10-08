from fastapi import FastAPI, Body

app = FastAPI()


@app.post("/items/")
def create_item(item: dict = Body(...)):
    return {"item": item}


@app.post("/advanced_items/")
def create_advanced_item(
    item: dict = Body(
        default=None,
        example={"key": "value"},
        alias="item_alias",
        title="Sample Item",
        description="This is a sample item",
        deprecated=False,
    ),
    additional_info: dict = Body(
        default=None,
        example={"info_key": "info_value"},
        title="Additional Info",
        description="This is some additional information about the item",
        deprecated=False,
    ),
):
    return {"item": item, "additional_info": additional_info}
