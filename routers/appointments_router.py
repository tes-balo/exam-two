# # from datetime import datetime
# # from fastapi import APIRouter
# # from appointment import Appointment
# # from doctors_router import doctors
# # from schemas.response import Response

# # appointments_router = APIRouter()
# # appointments = []

# # # def verify_token(token: str):
# # # 	if token != 

# # @appointments_router.get("", status_code=200)
# # def get_appointments():
# # 	return Response(
# # 		msg="Appointments retrieved successfully",
# # 		data=appointments
# # 	)

# # @appointments_router.post("", status_code=201)
# # def create_appointment(appointment: Appointment):
# # 	app = Appointment(
# # 		appointment_id= len(appointments) + 1,
# # 		patient= await patientQueue,
# # 		doctor= await doctorQueue,
# # 		date= datetime.today()
# # 	)
# # 	for doctor in doctors:
# # 		if doctor.get("is_available"):
# # 		return Response(
# # 			msg=f"Appointment successfully booked with {doctor.get("name")}",
# # 			data=appointments
# # 		)
# # 	return Response(
# # 		msg="All Doctors have been booked, try again soon",
# # 		data=appointments
# # 	)


# from schemas.appointment import Appointment, AppointmentCreate
# from routers.doctors_router import doctors

# appointments: list[Appointment] = []

# def create_appointment(payload: AppointmentCreate):
# 	for doc in doctors:
# 		if doc.get("is_available"):
# 		# return Response(
# 		# 	msg=f"Appointment successfully booked with {doctor.get("name")}",
# 		# 	data=appointments
# 		# )
# 	# return Response(
# 	# 	msg="All Doctors have been booked, try again soon",
# 	# 	data=appointments
# 	# )
# 			appointment = Appointment(
# 				appointment_id= len(appointments) + 1,
# 				doctor=doc,
# 				**payload
# 			)

# 			appointments.append(appointment)

# 			return Response( # type: ignore
# 				msg=f"Appointment successfully booked with {doc.get("name")}",
# 				data=appointment.model_dump()
# 			)
		
# 		return Response( # type: ignore
# 				msg="All doctors have been booked, try again soon",
# 				data=appointments
# 			)

# # Refactor into 2 fuctions (isdoctoravailable and create appointment)ls