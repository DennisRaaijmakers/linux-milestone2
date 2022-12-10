from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/user")
def read_root():
    return {"Hello": "World"}