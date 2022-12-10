from fastapi import FastAPI, Query, Path
from mongoengine import Document, StringField, connect

app = FastAPI()
connect(db="name", host="mongodb", port=27017, username="dennis", password="abc123!")

#class
class Name(Document):
    name = StringField()


@app.get("/user")
async def user():
    name = Name.objects
    print ("TEST", name)
    return {"name" : name}

@app.get("/api/")
async def user1():
    return {"Welcome to API"}