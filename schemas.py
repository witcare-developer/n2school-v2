from datetime import datetime
from pydantic import BaseModel

# ParentStudent --------------------
class ParentStudentBase(BaseModel):
    cpf: int
    register: str
    first_name: str
    surname: str
    gender: str
    date_birth: datetime
    
class ParentStudentCreate(ParentStudentBase):
    address_id: int

class ParentStudent(ParentStudentBase):

    class Config:
        orm_mode = True
#-------------------------------------

# Student ----------------------------
class StudentBase(BaseModel):
    cpf: int
    enrollment: str
    first_name: str
    surname: str
    gender: str
    date_birth: datetime

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):

    class Config:
        orm_mode = True
# ------------------------------------------

# Responsible-------------------------------
class ResponsibleBase(BaseModel):
    parent_cpf: int
    student_cpf: int

class ResponsibleCreate(ResponsibleBase):
    pass

class Responsible(ResponsibleBase):

    parent: list[ParentStudent] = []
    student: list[Student] = []

    class Config:
        orm_mode = True
#--------------------------------------------

# Address -----------------------------------
class AddressBase(BaseModel):

    public_place: str
    address_name: str
    number: str
    cep: str
    complement: str
    neighborhood: str
    city: str
    country: str

class AddressCreate(AddressBase):
    id: int

class Address(AddressBase):

    class Config:
        orm_mode = True