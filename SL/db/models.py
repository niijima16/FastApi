# 选课
from tortoise.models import Model
from tortoise import fields


class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="名前")
    pwd = fields.CharField(max_length=32, description="パスワード")
    sno = fields.IntField(description="学籍番号")

    # 一对多的关系
    clas = fields.ForeignKeyField("models.Clas", related_name="students")

    # 多对多的关系
    courses = fields.ManyToManyField("models.Course", related_name="students")


class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="授業名")
    teacher = fields.ForeignKeyField("models.Teacher", description="担任")
    addr = fields.CharField(max_length=32, description="教室", default="")


class Clas(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="クラス名")


class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="名前")
    pwd = fields.CharField(max_length=32, description="パスワード")
    tno = fields.IntField(description="教師番号")
