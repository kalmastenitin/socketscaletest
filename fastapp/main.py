from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

class Message(BaseModel):
    text = "hello fastapi"
    author = "john doe"


@app.get("/")
def hello():
    return {"message":"hello fastapi"}

@app.post("/")
def send_message(message:Message):
    text = message.text
    author = message.author
    response = {"status":"message received", "text":text, "author":author}
    return response
