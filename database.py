from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./n2school_db.db"
# "mysql:///?User=myUser&;Password=myPassword&Database=NorthWind&Server=myServer&Port=3306"
# mysql://scott:tiger@localhost/foo
# SQLALCHEMY_DATABASE_URL = "mysql:///?User=root&;Password=renatoyyz&Database=n2school_db&Server=localhost&Port=3306"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
