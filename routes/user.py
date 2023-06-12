from fastapi import APIRouter
from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity
from bson import ObjectId

user_router = APIRouter()

# get all the users
@user_router.get('/')
async def find_all_users():
    return usersEntity(conn.webApp.user.find())

# search one user
@user_router.get('/{id}')
async def find_one_user(id):
    return userEntity(conn.webApp.user.find_one({"_id":ObjectId(id)}))

# post user method
@user_router.post('/')
async def create_user(user: User):
    conn.webApp.user.insert_one(dict(user))
    return usersEntity(conn.webApp.user.find())

# update user
@user_router.put('/{id}')
async def update_user(id,user: User):
    conn.webApp.user.find_one_and_update({"_id": ObjectId(id)},{
        "$set":dict(user)
    })
    return userEntity(conn.webApp.user.find_one({"_id": ObjectId(id)}))

# delete user
@user_router.delete('/{id}')
async def delete_user(id):
    return userEntity(conn.webApp.user.find_one_and_delete({"_id":ObjectId(id)}))