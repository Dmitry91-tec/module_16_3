from fastapi import FastAPI,Path
from typing import Annotated, Set

app = FastAPI()

users = {"1": "Имя: Example,возраст: 18"}

@app.get("/users")
async def get_all_messages() -> dict:
    return users                               #возвращаем нашу базуданных
#
# @app.get("/message/{message_id}")
# async def get_message(message_id: str) -> dict:
#     return messages_db[message_id]

@app.post("/user/{username}/{age}")
async def create_message(username: str, age: int) -> str:
    current_index = str(int(max(users, key=int))+1)
    users[current_index] = f"username- {username}, age- {age}"
    return f"User {current_index} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_message(user_id: str, username: str, age: int) -> str:
    users[user_id] = f"username- {username}, age- {age}"
    return f"User {user_id} has been updated"

@app.delete("/user/{user_id}")
async def delete_message(user_id: str) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"