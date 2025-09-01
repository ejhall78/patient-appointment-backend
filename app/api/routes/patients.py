from fastapi import APIRouter, HTTPException
from app import crud, models

router = APIRouter(prefix="/patients", tags=["patients"])

@router.get("/")
async def root():
    return {"message": "Hello World, patients"}

@router.get("/{nhs_number}", response_model=models.PatientPublic)
async def get_patient(nhs_number):
    '''
    Retrieve patient by NHS Number.
    '''

    patient = crud.get_patient(nhs_number)
    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found.",
        )

    return patient

@router.post("/", response_model=models.PatientPublic)
async def create_patient(patient: models.PatientCreate):
    '''
    Create a new patient.
    '''

    patient_exists = crud.get_patient(patient.nhs_number)
    if patient_exists:
        raise HTTPException(
            status_code=400,
            detail="A patient with this NHS Number already exists in the database.",
        )

    return crud.create_patient(patient)

@router.patch("/", response_model=models.PatientPublic)
async def update_patient(patient: models.PatientUpdate):
    '''
    Update patient details.
    '''
    
    patient_exists = crud.get_patient(patient.nhs_number)
    if patient_exists is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found.",
        )

    return crud.update_patient(patient)

@router.delete("/{nhs_number}", response_model=models.Message)
async def delete_patient(nhs_number):
    '''
    Delete patient by NHS Number.
    '''

    res = crud.delete_patient(nhs_number)

    if res is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found.",
        )
    
    return res