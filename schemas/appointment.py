from datetime import datetime
from schemas.patients import Patient
from schemas.doctors import Doctor
from pydantic import BaseModel


class Appointment(BaseModel):
	appointment_id: int
	patient: Patient
	doctor: Doctor
	date: datetime

class AppointmentCreate(BaseModel):
	patient: Patient
	date: datetime

# class AppointmentUpdate(BaseModel):
# 	date: datetime