from fastapi_sqla import Base
from sqlalchemy import Column, Date, DateTime, Enum, Integer, String, func


class Doctor(Base):
    __tablename__ = "doctor"


class Patient(Base):
    __tablename__ = "patient"
    last_name = Column(String)

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.current_timestamp())
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    sex_at_birth = Column(
        Enum("FEMALE", "MALE", name="sex_at_birth_enum"), nullable=False
    )
    email = Column(String, nullable=False, unique=True)
