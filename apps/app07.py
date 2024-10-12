from fastapi import APIRouter

from pydantic import BaseModel, EmailStr
from typing import Union

app07 = APIRouter()

class UserIn(BaseModel):
    username : str
    password : str
    email : EmailStr
    full_name : Union[str, None] = None
    
class UserOut(BaseModel):
    username : str
    email : EmailStr
    full_name : Union[str, None] = None
    

@app07.post("/reg", response_model=UserOut)
async def reg(user: UserIn):
    return user