from typing import Union
from pipelines.langraph_example import  stream_graph_updates 
from models.input_models import Input

from fastapi import FastAPI
from settings import get_settings

app = FastAPI()
settings = get_settings()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/query/{question}")
def read_item(question: str,):
    return {"question": question}

@app.post("/try_graph/")
def try_graph(body :Input):
    # return {"question": body.text}
   return stream_graph_updates(body.text) 
