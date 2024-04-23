# from typing import Mapping
from fastapi import APIRouter, HTTPException
from src.schemas.doctors import (
	Doctor,
	DoctorCreate,
	DoctorUpdate
)

from src.schemas.response import Response

router = APIRouter()
doctors: dict[str, Doctor]  = {}
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
		"is_available": True,
		"email": "Josh@ymail.com"
	}
}

@router.get("", status_code=200)
def retrieve_doctors():
	# print(doctors)
	return Response(
		msg="All doctors",
		data=doctors
	)


@router.get("/{doctor_id}", status_code=200)
def retrieve_doctor(doctor_id: str):
	if doctor_id not in doctors:
		raise HTTPException(
			status_code=400,
			detail="doctor does not exist"
		)
	
	doctor = doctors[doctor_id]
	if not doctor:
		raise HTTPException(
			status_code=400,
			detail="doctor ID does not exist"
		)

	return Response(
		msg="doctor Found",
		data=doctor
	)

@router.post("", status_code=201)
def create_doctor(payload: DoctorCreate):
	doctor_id = str(len(doctors) + 1)

	if doctor_id in doctors:
		raise HTTPException(
			detail="doctor with the same id already exists",
			status_code=400
		)

	doctor = Doctor(
			doctor_id= doctor_id,
			**payload.model_dump()
		)
	
	doctors[doctor_id] = doctor
	print(doctors)

	return Response(
		msg="doctor Created Successfuly",
		data=doctor
	)

@router.put("/{doctor_id}", status_code=200)
def update_doctor(doctor_id: str, payload: DoctorUpdate):
	doctor_update = payload.model_dump()
	print(doctor_update)

	if doctor_id not in doctors:
		raise HTTPException(
			status_code=404,
			detail="doctor does not exist"
		)
	doctor = doctors[doctor_id]
	doctor["name"], doctor["phone"], doctor["email"], doctor["is_available"] = doctor_update.values()

	return Response(
		msg="doctor Updated Successfully",
		data=doctor
	)

@router.put("/appointments/{doctor_id}", status_code=200)
def toggle_availability(doctor_id: str):
	if doctor_id not in doctors:
		raise HTTPException(
			status_code=404,
			detail="doctor does not exist"
		)
	doctor = doctors[doctor_id]
	doctor["is_available"] = not doctor["is_available"]

	if not doctor["is_available"]:
		return Response(
			msg=f"Doctor {doctor["name"]} is now set to unavailable",
			data= doctor
		)

	return Response(
		msg=f"Doctor {doctor["name"]} is now set to available",
		data=doctor
	)