from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str
