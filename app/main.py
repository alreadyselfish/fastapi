from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
count = [1]


class User(BaseModel):
    username : str
    name : str
    age : int
    healthy : bool

allUsers = []


@app.get("/")
def root():
    return {'mssg':'succesfully installed and running'}

@app.get("/users")
def get_all_users():
    return {"data": allUsers}

@app.post("/users")
def create_user(user : User):
    user = user.model_dump()
    user['id'] = count[0]
    count[0] += 1
    allUsers.append(user)
    return {"data":"created user"}

@app.get("/users/{id}")
def get_one_user(id:int):
    user = None
    for u in allUsers:
        if u['id'] == id:
            user = u
            break 
    if not user:
        raise HTTPException(status_code=404, detail="id not found")
    return {"data":user}