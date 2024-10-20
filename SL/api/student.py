from fastapi import APIRouter, Request
from db.models import *
from pydantic import BaseModel, field_validator
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException
from typing import List, Union

student_api = APIRouter()


'''
フロントバックエンド分離式
'''
# class UserOut(BaseModel): # 通過チェック
#     name : str
#     sno : int
#     clas_id : int
#     id : int

# @student_api.get("/", response_model=list[UserOut])


@student_api.get("/")
async def getALLStudent():
    #     # (1)1全生徒情報サーチ
    # students = await Student.all()
    #     # print("students",students)
    #     # for stu in students:
    #     #     print("名前：",stu.name,"学籍番号:",stu.sno)

    #     # return {
    #     #     "Action": "Get all student information"
    #     # }

    #     # (2)特定の生徒をサーチ
    #     # student = await Student.filter(name="ZZZ")
    #     # print("ZZZ",student)

    #     # (3)Getでサーチ
    #     stu = await Student.get(name="ZZZ")
    #     print(stu.sno)

    #     # (4)非特定サーチ
    #     student = await Student.filter(sno__gt=1001)
    #     students = await Student.filter(sno__in=[1001,1002])
    #     print(student) # [<Student: 2>, <Student: 3>]
    #     print(students) # [<Student: 1>, <Student: 2>]

    #     # (5)valuesサーチ
    #     # students_values = await Student.all().values("name","sno") #辞書を返す
    #     students_values = await Student.filter(sno__range=[1,10000]) #Jsonを返す
    #     # students_values = await Student.filter(sno__range=[1, 10000]).values("name", "sno", "clas_id", "id") # listを返すことによってUseroutによるフィルターができるようになる

    #     return students_values
    students = await Student.all()
    Ano = await Student.get(name="Ano")
    Lin = await Student.get(name="Lin")

    print(Ano.name)
    print(await Ano.clas.values("name"))
    # students = await Student.all().values("name", "clas__name")

    print(await Ano.courses.all())
    print(await Lin.courses.all().values("name", "teacher__name"))

    students = await Student.all().values("name", "clas__name", "courses__name")

    return students


'''
フロントバックエンド分離しないやり方、テンプレにあるhtmlに渡す
'''
# @student_api.get("/index.html")
# async def getALLStudent(request: Request):
#     templates = Jinja2Templates(directory="templates")
#     students = await Student.all()

#     return templates.TemplateResponse(
#         "index.html", {
#             "request": request,
#             "students": students  # studentsデータをテンプレートに渡す
#         }
#     )

# ==================================================================================================


class StudentIn(BaseModel):
    name: str
    pwd: str
    sno: int
    clas_id: int
    courses: List[int] = []

    @field_validator("name")
    def name_must_alpha(cls, value):
        assert value.isalpha(), 'name must be alpha'
        return value

    @field_validator("sno")
    def sno_must_longer(cls, value):
        assert value > 1000 and value < 10000
        return value


@student_api.post("/")
async def addStudent(student_in: StudentIn):

    # データベースにアップデート
    # 方法1
    # student= Student(name=student_in.name,pwd=student_in.pwd,sno=student_in.sno,clas_id=student_in.clas_id)
    # await student.save()

    # 方法2 -- もっともよく使う方法
    student = await Student.create(name=student_in.name, pwd=student_in.pwd, sno=student_in.sno, clas_id=student_in.clas_id)

    # 3 == 3
    choose_courses = await Course.filter(id__in=student_in.courses)
    await student.courses.add(*choose_courses)

    return student


@student_api.get("/{student_id}")
async def getStudent(student_id: int):
    student = await Student.get(id=student_id)

    return student


@student_api.put("/{student_id}")
async def updateStudent(student_id: int, student_in: StudentIn):
    # データを辞書に変換し、coursesは別に取り出す
    data = student_in.model_dump()
    courses = data.pop("courses")

    # 学生情報の更新
    await Student.filter(id=student_id).update(**data)
    
    # コース情報の更新
    edit_stu = await Student.get(id=student_id)
    choose_courses = await Course.filter(id__in=courses)
    await edit_stu.courses.clear()  # 既存のコースをクリア
    await edit_stu.courses.add(*choose_courses)  # 新しいコースを追加

    # 更新した学生情報を辞書形式で返す
    return edit_stu


@student_api.delete("/{student_id}")
async def DeleteStudent(student_id: int):
    deleteCount = await Student.filter(id=student_id).delete()
    if not deleteCount:
        raise HTTPException(status_code=404,detail=f"Student:{student_id} not be created in database.")
    return {}
