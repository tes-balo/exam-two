from fastapi import APIRouter, HTTPException

from src.api.routes.doctors import doctors
from src.schemas.appointment import Appointment, AppointmentCreate

from src.schemas.response import Response
from src.schemas.patients import Patient, PatientCreate, PatientUpdate

router = APIRouter()
patients: dict[str, Patient]  = {}
appointments: dict[str, Appointment] = {}

@router.get("", status_code=200)
def retrieve_patients():
	# print(patients)
	return {"data": patients}


@router.get("/{patient_id}", status_code=200)
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

@router.post("", status_code=201)
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

@router.put("/{patient_id}")
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

@router.get("/appointments", status_code=200)
def get_appointments():
	return Response(
		msg="All appointments",
		data=appointments
	)

@router.post("/appointments", status_code=201)
def create_appointment(payload: AppointmentCreate):
	print('test')
	for doc in doctors:
		if not doctors[doc]["is_available"]:
			raise HTTPException(
				status_code=404,
				detail={
					"msg":"No doctor available",
					"data":doctors}
			)
		
		appointment_id = str(len(appointments) + 1)

		print("test2")
		appointment = Appointment(
			appointment_id=appointment_id,
			doctor=doctors[doc],
			**payload.model_dump()
		)

		appointments[appointment_id] = appointment

		doctors[doc]["is_available"] = False

		return Response(
			msg=f"Appointment successfully booked with {doctors[doc].get("name")}",
			data=appointment
		)
	

@router.put("/appointments/{appointment_id}", status_code=200)
def complete_appointment(appointment_id: str):
	if appointment_id not in appointments:
		raise HTTPException(
			status_code=404,
			detail="Appointment does not exist"
		)
	completed_appointment = appointments[appointment_id]
	appointments[appointment_id]["doctor"]["is_available"] = True

	return Response(
		msg="Appointment completed",
		data=completed_appointment
	)


	
@router.delete("/appointments/{appointment_id}", status_code=200)
def cancel_appointment(appointment_id: str):
	if appointment_id not in appointments:
		raise HTTPException(
			status_code=404,
			detail="Appointment does not exist"
		)
	
	cancelled_appointment = appointments[appointment_id]
	del appointments[appointment_id]

	return Response(
		msg="Appointment successfully cancelled",
		data=cancelled_appointment
	)

# Refactor into 2 fuctions (isdoctoravailable and create appointment)

# def complete_appointment(id: int,):

# @patients_router.put("/appointments/{id}", status_code= 300)
# why doesnt python allow hyphens in path params
# def complete_ap(id: int):
# 	for ap in appointments:
# 		if ap[]
