from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/query/{question}")
def read_item(question: str,):
    return {"question": question}
