from sqlmodel import Session, select
from app.core.db import engine
from app.models import Patient, PatientCreate, PatientPublic, PatientUpdate, Message

def get_patient(nhs_number: str) -> PatientPublic | None:
    with Session(engine) as session:
        statement = select(Patient).where(Patient.nhs_number == nhs_number)
        results = session.exec(statement)
        patient = results.first()

        if patient is None:
            return None

        patient_public = PatientPublic(
            nhs_number=patient.nhs_number,
            name=patient.name,
            date_of_birth=patient.date_of_birth,
            postcode=patient.postcode,
        )

        return patient_public

def create_patient(patient_create: PatientCreate):
    with Session(engine) as session:
        db_patient = Patient.model_validate(patient_create)
        session.add(db_patient)
        session.commit()
        session.refresh(db_patient)
        return db_patient
    
def update_patient(patient_update: PatientUpdate) -> PatientPublic | None:
    with Session(engine) as session:
        statement = select(Patient).where(Patient.nhs_number == patient_update.nhs_number)
        results = session.exec(statement)
        db_patient = results.first()

        if db_patient is None:
            return None

        patient_update_data = patient_update.model_dump(exclude_unset=True)

        db_patient.sqlmodel_update(patient_update_data)

        session.add(db_patient)
        session.commit()
        session.refresh(db_patient)

        patient_public = PatientPublic(
            nhs_number=db_patient.nhs_number,
            name=db_patient.name,
            date_of_birth=db_patient.date_of_birth,
            postcode=db_patient.postcode,
        )

        return patient_public

def delete_patient(nhs_number: str) -> Message | None:
    with Session(engine) as session:
        statement = select(Patient).where(Patient.nhs_number == nhs_number)
        results = session.exec(statement)
        patient = results.first()

        if patient is None:
          return None

        session.delete(patient)
        session.commit()

        return Message(message="Patient deleted successfully.")