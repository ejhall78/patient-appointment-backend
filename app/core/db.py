from sqlmodel import SQLModel, create_engine
# import os

# db_url = f"postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@db:5432/{os.getenv("POSTGRES_DB")}"
db_url = "postgresql://postgres:changethis@db:5432/app"
print(db_url)

engine = create_engine(db_url, echo=True)