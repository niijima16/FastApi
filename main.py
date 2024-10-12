from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles

from apps.app07 import app07

app = FastAPI()

app.mount("/static", StaticFiles(directory="statics"))


app.include_router(app07, tags=["07 响应参数"])

if __name__ == '__main__':
    uvicorn.run("main:app", port=8090, debug=True, reload=True)