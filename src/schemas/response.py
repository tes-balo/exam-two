from typing import Any
from src.schemas.doctors import Doctor
from src.schemas.appointment import Appointment
from src.schemas.patients import Patient
from pydantic import BaseModel

class Response(BaseModel):
	msg: str
	data: list[Appointment] | list[Patient] | list[Doctor] | Patient | Doctor | Appointment | dict[str, Any]
	has_error: bool = False
	error_msg: str | None = None