from fastapi import FastAPI
from fastapi.responses import (
    JSONResponse,
    HTMLResponse,
    PlainTextResponse,
    RedirectResponse,
)

app = FastAPI()


@app.get("/json", response_class=JSONResponse)
def read_json():
    return {"msg": "This is JSON"}


@app.get("/html", response_class=HTMLResponse)
def read_html():
    return "<h1>This is HTML</h1>"


@app.get("/text", response_class=PlainTextResponse)
def read_text():
    return "This is plain text"


@app.get("/redirect", response_class=RedirectResponse)
def redirect():
    return RedirectResponse(url="/json")
