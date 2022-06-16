from sqlalchemy.orm import Session

from . import models, schemas

def get_parent(db: Session, parent_cpf: int):
    return db.query(models.User).filter(models.ParentStudent.cpf == parent_cpf).first()

def create_parent_student(db: Session, item: schemas.StudentCreate, parent_cpf: int):
    db_parent = models.Student(**item.dict())
    db.add(db_parent)
    db.commit()
    db.refresh(db_parent)
    return db_parent