from typing import Union
from pydantic import BaseModel, Field
from fastapi import FastAPI

app = FastAPI()

connect(db="name", host="mongodb", port=27017, username="dennis", password="abc123!")

class UserBase(MongoBase):
    name: str


@app.get('/user', response_model=users.UserBase)
async def namedb():
    name = await db.users.find()
    return name
