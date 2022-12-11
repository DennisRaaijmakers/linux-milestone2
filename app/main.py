from typing import Union
from pydantic import BaseModel, Field
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

mongodb_uri = 'mongodb://dennis:abc123!@nginx.net/milestone2.collection'
port = 27017

client = MongoClient(mongodb_uri, port)

class UserBase(BaseModel):
    name: str


@app.get('/user', response_model=UserBase)
async def namedb():
    name = await db.milestone2.find()
    return name
