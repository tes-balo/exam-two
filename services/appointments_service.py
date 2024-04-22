from fastapi import HTTPException
from schemas.appointment import Appointment, AppointmentCreate
from schemas.response import Response
# from routers.appointments_router import appointments
from routers.doctors_router import doctors

appointments: list[Appointment] = []

	# return Response(
		# 	msg=f"Appointment successfully booked with {doctor.get("name")}",
		# 	data=appointments
		# )
	# return Response(
	# 	msg="All Doctors have been booked, try again soon",
	# 	data=appointments
	# )

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
	
		print("test2")
		appointment = Appointment(
			appointment_id= len(appointments) + 1,
			doctor=doctors[doc],
			**payload.model_dump()
		)

		appointments.append(appointment)

		return Response(
			msg=f"Appointment successfully booked with {doctors[doc].get("name")}",
			data=appointment.model_dump()
		)
	
# def cancel_appointment(id: str):
# 	if id not in appointments:
# 		# 
	
		
		# raise HTTPException(
		# 	detail="No Doctor available",
		# 	status_code=404
		# )

		# return Response(
		# 		msg="All doctors have been booked, try again soon",
		# 		data=appointments
		# 	)

# Refactor into 2 fuctions (isdoctoravailable and create appointment)

# def complete_appointment(id: int,):