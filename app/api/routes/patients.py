from fastapi import APIRouter
from app import crud

router = APIRouter(prefix="/patients", tags=["patients"])

@router.get("/")
async def root():
    return {"message": "Hello World, patients"}

@router.get("/{nhs_number}")
async def get_patient(nhs_number):
    return crud.get_patient(nhs_number)