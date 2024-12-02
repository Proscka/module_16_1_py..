from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def welcome()-> dict:
    return {f"Главная страница"}

@app.get("/user/admin")
async def administrator()-> dict:
    return {f"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_number(user_id:int)->dict:
    return (f"Вы вошли как пользователь №{user_id}")

@app.get('/user')
async def user_info(username: str,age:int)->dict:
        return(f"Информация о пользователе. Имя:{username}, возраст:{age}")