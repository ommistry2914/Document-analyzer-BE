from fastapi import APIRouter, Body
from auth import register_user, login_user

router = APIRouter(prefix="/auth")

@router.post("/register")
async def register(email: str = Body(...), password: str = Body(...)):
    user_id = await register_user(email, password)
    return {"user_id": user_id, "message": "Registered successfully"}

@router.post("/login")
async def login(email: str = Body(...), password: str = Body(...)):
    token = await login_user(email, password)
    return {"access_token": token}
