import uvicorn
from fastapi import FastAPI



app = FastAPI()



@app.get("/user")
def get_user():
    return {
        "user":"current user"
    }
    

    
if __name__ == '__main__':
    uvicorn.run("main:app", port=8090, reload=True)