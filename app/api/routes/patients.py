from fastapi import APIRouter, HTTPException
import datetime
from app import crud, models
from ...utils import postcode
import nhs_number as nhs_number_util

router = APIRouter(prefix="/patients", tags=["patients"])

@router.get("/")
async def root():
    return {"message": "Hello World, patients"}

@router.get("/{nhs_number}", response_model=models.PatientPublic)
async def get_patient(nhs_number):
    '''
    Retrieve patient by NHS Number.
    '''

    if not nhs_number_util.is_valid(nhs_number):
        raise HTTPException(
            status_code=400,
            detail="Please enter a valid NHS Number."
        ) 

    normalised_nhs_number = nhs_number_util.normalise_number(nhs_number)

    patient = crud.get_patient(normalised_nhs_number)
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

    if not nhs_number_util.is_valid(patient.nhs_number):
        raise HTTPException(
            status_code=400,
            detail="Please enter a valid NHS Number."
        )

    patient.nhs_number = nhs_number_util.normalise_number(patient.nhs_number)

    if not postcode.valid_postcode(patient.postcode):
        raise HTTPException(
            status_code=400,
            detail="Please enter a valid postcode format."
        )
    
    patient.postcode = postcode.format_valid_postcode(patient.postcode)

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

    if not nhs_number_util.is_valid(patient.nhs_number):
        raise HTTPException(
            status_code=400,
            detail="Please enter a valid NHS Number."
        )
    
    patient.nhs_number = nhs_number_util.normalise_number(patient.nhs_number)

    if patient.postcode is not None:
        if not postcode.valid_postcode(patient.postcode):
            raise HTTPException(
                status_code=400,
                detail="Please enter a valid postcode format."
            )
        patient.postcode = postcode.format_valid_postcode(patient.postcode)
        
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

    if not nhs_number_util.is_valid(nhs_number):
        raise HTTPException(
            status_code=400,
            detail="Please enter a valid NHS Number."
        ) 

    normalised_nhs_number = nhs_number_util.normalise_number(nhs_number)    

    res = crud.delete_patient(normalised_nhs_number)

    if res is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found.",
        )
    
    return res

# TODO: refactor. This is a very rudimentary integration test.
# An end-to-end test involving the frontend would be more valuable.
@router.post("/intergration-test", response_model=models.Message)
async def run_integration_test(patient: models.PatientCreate):
    '''
    Run a full CRUD integration test.
    '''

    created_patient = await create_patient(patient=patient)
    fetched_patient = await get_patient(created_patient.nhs_number)
    await update_patient(models.PatientUpdate(
        nhs_number=fetched_patient.nhs_number,
        name="Updated Name",
        date_of_birth=datetime.date(2000, 1, 1),
        postcode="N1 1AA"
    ))
    successfully_deleted = await delete_patient(patient.nhs_number)

    if successfully_deleted.message != "Patient deleted successfully.":
        return models.Message(message="FAIL - Patient integration test unsuccessful.")

    return models.Message(message="PASS - Patient integration test successful.")