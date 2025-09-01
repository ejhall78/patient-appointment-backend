from fastapi import APIRouter
from app import crud, models

router = APIRouter(prefix="/patients", tags=["patients"])

@router.get("/")
async def root():
    return {"message": "Hello World, patients"}

@router.get("/{nhs_number}", response_model=models.PatientPublic)
async def get_patient(nhs_number):
    return crud.get_patient(nhs_number)

@router.post("/", response_model=models.PatientPublic)
async def create_patient(patient: models.PatientCreate):
    return crud.create_patient(patient)