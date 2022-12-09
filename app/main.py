from fastapi import FastAPI, Query, Path
from mongoengine import Document, StringField, connect
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
connect(db="name", host="mongodb", port=27017, username="dennis", password="abc123!")
# CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#class
class Name(Document):
    name = StringField()


@app.get("/user")
def user():
    name = Name.objects
    return name
