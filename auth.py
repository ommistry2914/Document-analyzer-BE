from fastapi import HTTPException
from database import users_collection
from utils.security import hash_password, verify_password, create_access_token
from bson import ObjectId

async def register_user(firstName: str, lastName: str, email: str, password: str):
    existing = await users_collection.find_one({"email": email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = hash_password(password)
    user = {
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "password": hashed,
    }
    result = await users_collection.insert_one(user)
    return str(result.inserted_id)

async def login_user(email: str, password: str):
    user = await users_collection.find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"user_id": str(user["_id"])})
    user_data = {
        "id": str(user["_id"]),
        "firstName": user["firstName"],
        "lastName": user["lastName"],
        "email": user["email"],
    }
    return token, user_data
