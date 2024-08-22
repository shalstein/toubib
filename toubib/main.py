from datetime import date
from importlib.metadata import version

import fastapi_sqla
from fastapi import Depends, FastAPI, HTTPException
from fastapi_sqla import Item, Session, Page, Paginate
from pydantic import BaseModel, EmailStr
from structlog import get_logger
from enum import Enum
from .sqla import Doctor, Patient
from sqlalchemy import select, func


log = get_logger()

app = FastAPI(title="toubib", version=version("toubib"))

fastapi_sqla.setup(app)


@app.get("/health")
def health():
    "Return OK if app is reachable"
    return "OK"


class DoctorIn(BaseModel):
    first_name: str
    last_name: str
    hiring_date: date
    specialization: str


class DoctorModel(DoctorIn):
    id: int

    class Config:
        orm_mode = True


class GenderEnum(str, Enum):
    female = "FEMALE"
    male = "MALE"


class PatientIn(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    date_of_birth: date
    sex_at_birth: GenderEnum


class PatientModel(PatientIn):
    id: int

    class Config:
        orm_mode = True


@app.post("/v1/doctors", response_model=Item[DoctorModel], status_code=201)
def create_doctor(*, body: DoctorIn, session: Session = Depends()):
    doctor = Doctor(**body.dict())
    session.add(doctor)
    session.flush()
    return {"data": doctor}


@app.get("/v1/doctors/{doctor_id}", response_model=Item[DoctorModel])
def get_doctor(*, doctor_id: int, session: Session = Depends()):
    doctor = session.get(Doctor, doctor_id)
    if doctor is None:
        raise HTTPException(404)
    return {"data": doctor}


@app.get("/v1/patients", response_model=Page[PatientModel])
def list_patients(paginate=Depends(Paginate)):
    return paginate(select(Patient).order_by(func.lower(Patient.last_name)))


@app.post("/v1/patients", response_model=Item[PatientModel], status_code=201)
def create_patient(*, body: PatientIn, session: Session = Depends()):
    patient = Patient(**body.dict())
    session.add(patient)
    session.flush()
    return {"data": patient}


@app.get("/v1/patients/{patient_id}", response_model=Item[PatientModel])
def get_patient(patient_id: int, session: Session = Depends()):
    patient = session.get(Patient, patient_id)
    if patient is None:
        raise HTTPException(404)
    return {"data": patient}
