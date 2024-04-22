from typing import Mapping
from fastapi import APIRouter

from schemas.doctors import Doctor

doctors_router = APIRouter()
# doctor_id: int
# 	name: str
# 	specialization: str
# 	phone: str
# 	is_available: bool = True
# 	email: str
doctors: dict[str, Doctor] = {
	"1": {
		"doctor_id": "d1",
		"name": "Josh",
		"specialization": "Orthodontist",
		"phone": "+9126252281",
		"is_available": True,
		"email": "Josh@ymail.com"
	},
	"2": {
		"doctor_id": "d2",
		"name": "Brian",
		"specialization": "Chemist",
		"phone": "+9126252281",
		"is_available": False,
		"email": "Josh@ymail.com"
	}
}

@doctors_router.get("", status_code=200)
def get_index():
	return {"data": "home works"}

# @doctors_router.post("/new", status_code=201)
# def create_doctor(payload):
