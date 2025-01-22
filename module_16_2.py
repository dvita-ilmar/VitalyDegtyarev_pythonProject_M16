"""
coding: utf-8
Дегтярев Виталий (группа 22/08)
Домашнее задание №16.2
Домашнее задание по теме "Валидация данных"
"""

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


# Маршрут к главной странице
@app.get("/")
async def root() -> dict:
    return {"message":"Главная страница"}


# Маршрут к "/user/admin"
@app.get("/user/admin")
async def get_admin() -> dict:
    return {"message":"Вы вошли как администратор"}


# Маршрут к "/user/{user_id}"
@app.get("/user/{user_id}")
async def get_user(user_id:Annotated[int, Path(ge=1, le=100, description="Enter User ID")]):
    return {"message":f"Вы вошли как пользователь № {user_id}"}


# Маршрут к "/user/{username}/{age}" (Не получается прикрутить валидацию данных к маршруту вида "/user<?username=&age=>" - почему?)
@app.get("/user/{username}/{age}")
async def get_user_info(
                        username:Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                        age:Annotated[int, Path(ge=18, le=120, description="Enter age")]
                        ):
    return {"Информация о пользователе. Имя":username, "Возраст":age}