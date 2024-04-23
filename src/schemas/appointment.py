from datetime import datetime
from typing import TypedDict
from src.schemas.patients import Patient
from src.schemas.doctors import Doctor
from pydantic import BaseModel


class Appointment(TypedDict):
	appointment_id: str
	patient: Patient
	doctor: Doctor
	date: datetime

class AppointmentCreate(BaseModel):
	patient: Patient
	date: datetime