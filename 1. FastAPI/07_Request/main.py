from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
def read_items(
    string_query: str = Query(
        default="default value",
        min_length=2,
        max_length=5,
        regex="^[a-zA-Z]+$",
        title="String Query",
        example="abc",
        description="A simple string query",
        alias="str-query",
    ),
    number_query: float = Query(
        default=1.0,
        ge=0.5,
        le=10.5,
        title="Number Query",
        example=5.5,
        alias="num-query",
        deprecated=True,
    ),
):
    return {"string_query_handled": string_query, "number_query_handled": number_query}
