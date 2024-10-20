from fastapi import FastAPI
from fastapi.responses import Response
from fastapi import Request
import uvicorn


app = FastAPI()

@app.middleware("http")
async def m2(request:Request,call_next):
    # Request_ZOOM
    print("m2 reqeust")
    res = await call_next(request)
    res.headers["author"] = "Skadi"
    print("m2 reqeust")
    
    # Response_ZOOM
    print("m2 resoonse")
    
    return res

@app.middleware("http")
async def m1(request:Request,call_next):
    # Request_ZOOM
    print("m1 reqeust")
    
    # if request.client.host in ["127.0.0.1",]:
    #     return Response(content="visit forbibian")
    if request.url.path in ["/user"]:
        return Response(content="visit forbibian")
        
    res = await call_next(request)
    
    # Response_ZOOM
    print("m1 resoonse")
    
    return res


@app.get("/user")
def get_user():
    print("run get_user")
    return {
        "user":"current user"
    }
    
@app.get("/item/{item_id}")
def get_item(item_id: int):
    print("run get_item")
    return {
        "item_id": item_id
    }
    
if __name__ == '__main__':
    uvicorn.run("main:app", port=8090, reload=True)