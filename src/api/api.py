from fastapi import APIRouter 
from .routes import (
	patients,
	doctors
)

api_router = APIRouter()

api_router.include_router(patients.router, prefix="/patients", tags=["Patients"])
api_router.include_router(doctors.router, prefix="/doctors", tags=["Doctors"])