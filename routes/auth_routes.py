from fastapi import APIRouter, Body
from auth import register_user, login_user

router = APIRouter(prefix="/auth")

@router.post("/register")
async def register(
    firstName: str = Body(...),
    lastName: str = Body(...),
    email: str = Body(...),
    password: str = Body(...)
):
    await register_user(firstName, lastName, email, password)
    return {"message": "Registered successfully"}

@router.post("/login")
async def login(
    email: str = Body(...),
    password: str = Body(...)
):
    token, user = await login_user(email, password)
    return {"access_token": token, "user": user}


