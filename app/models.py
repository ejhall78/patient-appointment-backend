import datetime
from sqlmodel import SQLModel, Field

class PatientBase(SQLModel):
    nhs_number: str = Field(index=True)
    name: str
    date_of_birth: datetime.date
    postcode: str

class Patient(PatientBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class PatientPublic(PatientBase):
    pass

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    name: str | None = None
    date_of_birth: datetime.date | None = None
    postcode: str | None = None

# Generic message
class Message(SQLModel):
    message: str