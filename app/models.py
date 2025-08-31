from sqlmodel import SQLModel, Field

class Patient(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nhs_number: int
    name: str
    date_of_birth: str
    postcode: str