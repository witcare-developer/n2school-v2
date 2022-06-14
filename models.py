from datetime import date
from email.policy import default
from xmlrpc.client import DateTime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class ParentStudent(Base):
    __tablename__ = "parent_student"

    cpf = Column(Integer, primary_key=True, index=True, autoincrement=False)
    register = Column(String, unique=True, index=True)
    first_name = Column(String)
    surname = Column(String)
    gender = Column(String)
    date_birth = Column(DateTime)
    address_id = Column(Integer, ForeignKey("address.id"))

    student_item = relationship("Responsible", back_populates="parent")

class Student(Base):
    __tablename__ = "student"

    cpf = Column(Integer, primary_key=True, index=True, autoincrement=False)
    enrollment = Column(String, unique=True)
    first_name = Column(String)
    surname = Column(String)
    gender = Column(String)
    date_birth = Column(DateTime)

    parent_item = relationship("Responsible", back_populates="student")


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    public_place = Column(String)
    address_name = Column(String)
    number = Column(String)
    cep = Column(String)
    complement = Column(String, default="N/A")
    neighborhood = Column(String)
    city = Column(String)
    country = Column(String)

class Responsible(Base):
    __tablename__ = "responsible"
    parent_cpf = Column(Integer, ForeignKey("parent_student.cpf"))
    student_cpf = Column(Integer, ForeignKey("student.cpf") )

    parent = relationship("ParentStudent", back_populates="student_item")
    student = relationship("Student", back_populates="parent_item")