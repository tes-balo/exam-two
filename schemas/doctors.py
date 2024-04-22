from typing_extensions import TypedDict
from pydantic import BaseModel

class Doctor(TypedDict):
	doctor_id: str
	name: str
	specialization: str
	phone: str
	is_available: bool
	email: str

# class Doctors(BaseModel):
# 	id: str
# 	doctor: Doctor

class DoctorCreate(BaseModel):
	name: str
	specialization: str
	phone: str
	is_available: bool = True
	email: str

class DoctorUpdate(BaseModel):
	name: str
	phone: str
	email: str
	is_available: bool = True