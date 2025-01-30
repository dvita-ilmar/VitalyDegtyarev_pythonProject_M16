"""
coding: utf-8
Дегтярев Виталий (группа 22/08)
Домашнее задание №16.3
Домашнее задание по теме "CRUD Запросы: Get, Post, Put Delete."
"""


from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

# Чтение (Read) и выдача в браузер списка пользователей
@app.get("/users")
async def get_all_users() -> dict:
    return users

# Создание (Create) нового пользователя
@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
                      ) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return f"User {current_index} is registered"

# Обновление (Update) данных конкретного пользователя
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")],
                      username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
                      ) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is updated"

# Удаление (Delete) конкретного пользователя
@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]) -> str:
    users.pop(str(user_id))
    return f"User {user_id} has been deleted"