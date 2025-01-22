"""
coding: utf-8
Дегтярев Виталий (группа 22/08)
Домашнее задание №16.1
Домашнее задание по теме "Основы Fast Api и маршрутизация"
"""

from fastapi import FastAPI

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
async def get_user(user_id:int) -> dict:
    return {"message":f"Вы вошли как пользователь № {user_id}"}


# Маршрут к "/user"
@app.get("/user")
async def get_user_info(username: str, age: int) -> dict:
    return {"Информация о пользователе. Имя":username, "Возраст":age}