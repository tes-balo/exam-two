from fastapi import FastAPI
from routers.doctors_router import doctors_router
from routers.patients_router import patients_router
app = FastAPI()

app.include_router(patients_router, prefix="/patients", tags=["Patients"])
app.include_router(doctors_router, prefix="/doctors", tags=["Doctors"])
# app.include_router(patients_router, prefix="/patients", tags=["Patients"])
