from sqlmodel import Session, select
from app.core.db import engine
from app.models import Patient, PatientCreate, PatientPublic

def get_patient(nhs_number: str) -> PatientPublic:
    with Session(engine) as session:
            statement = select(Patient).where(Patient.nhs_number == nhs_number)
            results = session.exec(statement)
            patient = results.one()
            patient_public = PatientPublic(nhs_number=patient.nhs_number, name=patient.name, date_of_birth=patient.date_of_birth, postcode=patient.postcode)
            return patient_public

def create_patient(patient: PatientCreate):
    with Session(engine) as session:
        db_patient = Patient.model_validate(patient)
        session.add(db_patient)
        session.commit()
        session.refresh(db_patient)
        return db_patient