import email
import random
from fastapi import APIRouter, HTTPException

from schemas.appointment import Appointment, AppointmentCreate
from services.appointments_service import create_appointment
from schemas.response import Response
from schemas.patients import P, Patient, PatientCreate, PatientUpdate
patients_router = APIRouter()
patients: dict[str, Patient]  = {}
appointments: list[Appointment] = []

@patients_router.get("", status_code=200)
def retrieve_patients():
	# print(patients)
	return {"data": patients}


@patients_router.get("/{patient_id}", status_code=200)
def retrieve_patient(patient_id: str):
	if patient_id not in patients:
		raise HTTPException(
			status_code=400,
			detail="Patient does not exist"
		)
	
	patient = patients[patient_id]
	# if not patient:
	# 	raise HTTPException(
	# 		status_code=400,
	# 		detail="Patient ID does not exist"
	# 	)

	return Response(
		msg="Patient Found",
		data=patient
	)

@patients_router.post("", status_code=201)
def create_patient(payload: PatientCreate):
	# pay = payload.model_dump()

	patient_id = str(len(patients) + 1)


	if patient_id in patients:
		raise HTTPException(
			detail="Patient with the same id already exists",
			status_code=400
		)


	patient = Patient(
			patient_id= patient_id,
			**payload.model_dump()
		)
	
	patients[patient_id] = patient
	# print(patients)

	return Response(
		msg="Patient Created Successfuly",
		data=patient
	)

@patients_router.put("/{patient_id}")
def update_patient(patient_id: str, payload: PatientUpdate):
	patient_update = payload.model_dump()
	# print(patient_update)

	if patient_id not in patients:
		raise HTTPException(
			status_code=404,
			detail="Patient does not exist"
		)
	patient = patients[patient_id]
	# print(patient)
	
	patient["name"], patient["weight"], patient["height"], patient["phone"], patient["email"] = patient_update.values()

	return Response(
		msg="Patient Updated Successfully",
		data=patient
	)

@patients_router.get("/appointments", status_code=200)
def get_appointments():
	return Response(
		msg="All appointments",
		data=appointments
	)

@patients_router.post("/appointments", status_code=201)
def create_ap(payload: AppointmentCreate):
	return create_appointment(payload)
# @patients_router.put("/appointments/{id}", status_code= 300)
# why doesnt python allow hyphens in path params
# def complete_ap(id: int):
# 	for ap in appointments:
# 		if ap[]
