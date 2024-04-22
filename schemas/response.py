from typing import Any
from schemas.appointment import Appointment
from schemas.doctors import Doctor
from schemas.patients import Patient
from pydantic import BaseModel

class Response(BaseModel):
	msg: str
	data: list[Appointment] | list[Patient] | list[Doctor] | Patient | Doctor | Appointment | dict[str, Any]
	has_error: bool = False
	error_msg: str | None = None