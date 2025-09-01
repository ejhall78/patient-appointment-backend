from sqlmodel import Session, select
from app.core.db import engine
from app.models import Patient

def get_patient(nhs_number: str) -> Patient:
  with Session(engine) as session:
          statement = select(Patient).where(Patient.nhs_number == nhs_number)
          results = session.exec(statement)
          patient = results.one()
          return patient