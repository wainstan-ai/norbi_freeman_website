from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import databases
import sqlalchemy

DATABASE_URL = "mysql://user:password@localhost/dbname"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/api/message")
async def create_message(msg: Message):
    query = "INSERT INTO messages (message) VALUES (:message)"
    await database.execute(query=query, values={"message": msg.message})
    return {"status": "Сообщение отправлено!"}

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()