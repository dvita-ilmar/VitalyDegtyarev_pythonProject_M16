"""
coding: utf-8
Дегтярев Виталий (группа 22/08)
Домашнее задание №16.4
Домашнее задание по теме "Модели данных Pydantic"
"""

from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

users = []

class User(BaseModel):
    id: int = None #Field(..., description="Идентификатор пользователя")
    username: str = Field(..., min_length=5, max_length=20, description="Имя пользователя")
    age: int = Field(..., ge=1, le=120, description="Возраст пользователя")


# Чтение (Read) и выдача в браузер списка пользователей
@app.get("/users")
async def get_all_users() -> List[User]:
    return users

# Создание (Create) нового пользователя
@app.post("/user/{username}/{age}")
async def create_user(user: User):
    user.id = len(users) + 1
    users.append(user)
    return user

# Обновление (Update) данных конкретного пользователя
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user: User):
    for edit_user in users:
        if edit_user.id == user.id:
            edit_user.username  = user.username
            edit_user.age = user.age
            return user
    raise HTTPException(404, "User was not found")

# Удаление (Delete) конкретного пользователя
@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    for i, deleting_user in enumerate(users):
        if deleting_user.id == user_id:
            del users[i]
            return deleting_user
    raise HTTPException(404, "User was not found")