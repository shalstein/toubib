from fastapi_sqla import Base
from sqlalchemy import Column, String


class Doctor(Base):
    __tablename__ = "doctor"


class Patient(Base):
    __tablename__ = "patient"
    last_name = Column(String)
