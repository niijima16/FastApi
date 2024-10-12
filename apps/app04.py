from fastapi import APIRouter

from fastapi import Form

app04 = APIRouter()


@app04.post("/regin")
async def regin(username: str = Form(), password: str = Form()):
    print(f"username: {username}, Password: {password}")
    return {
        "username": username
    }
