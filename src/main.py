from fastapi import FastAPI
from src.api.api import api_router
app = FastAPI()

app.include_router(api_router)

@app.get("/home")
def home():
    return {"message": "ok!"}