from fastapi import FastAPI
import os
from models import Patient
from sqlmodel import create_engine, Session, select

app = FastAPI()

# db_url = f"postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@db:5432/{os.getenv("POSTGRES_DB")}"
db_url = "postgresql://postgres:changethis@db:5432/app"
print(db_url)

engine = create_engine(db_url, echo=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/patients/{nhs_number}")
async def get_patient(nhs_number):
    with Session(engine) as session:
        statement = select(Patient).where(Patient.nhs_number == nhs_number)
        results = session.exec(statement)
        patient = results.one()
        return patient