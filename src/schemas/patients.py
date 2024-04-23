from typing_extensions import TypedDict
from pydantic import BaseModel
# Patient: id, name, age, sex, weight, height, phone
# Doctors: id, name, specialization, phone, is_available (defaults to True)
# Appointment: id, patient, doctor, date

class Patient(TypedDict):
	patient_id: str
	name: str
	age: int
	sex: str
	weight: float
	height: float
	phone: str
	email: str

class PatientCreate(BaseModel):
	name: str
	age: int
	sex: str
	weight: float
	height: float
	phone: str
	email: str

class PatientUpdate(BaseModel):
	name: str
	weight: float
	height: float
	phone: str
	email: str