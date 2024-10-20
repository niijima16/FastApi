import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# @app.middleware("http")
# async def TestCORS(request:Request,call_next):
#     response = await call_next(request)
#     response.headers["Acess-Control-Allow-Orrgin"] = "*"
    
#     return response

origins = [
    "http://localhost:8060"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/user")
def get_user():
    print("come from outside")
    return {
        "user":"Skadi"
    }

    

    
if __name__ == '__main__':
    uvicorn.run("main:app", port=8090, reload=True)