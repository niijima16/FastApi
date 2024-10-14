import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM
from api.student import student_api

app = FastAPI()
templates = Jinja2Templates(directory="\\SL\\templates")


app.include_router(student_api,prefix="/student", tags=["履修登録システム"])


register_tortoise(
    app=app,
    config=TORTOISE_ORM,
)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1',
                port=8010, reload=True, workers=1)
