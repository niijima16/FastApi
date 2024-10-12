from fastapi import APIRouter

student_api = APIRouter()


@student_api.get("/")
async def getALLStudent():
    return {
        "Action": "Get all student information"
    }


@student_api.post("/")
async def addStudent():

    return {
        "Action": "Add a student data"
    }


@student_api.get("/{student_id}")
async def getStudent(student_id: int):

    return {
        "Action": f"Search a id={student_id} student data"
    }


@student_api.put("/{student_id}")
async def updateStudent(student_id: int):

    return {
        "Action": f"Update a id={student_id} student data"
    }


@student_api.delete("/{student_id}")
async def DeleteStudent(student_id: int):

    return {
        "Action": f"Deletd a id={student_id} student data"
    }
