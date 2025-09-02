from sqlmodel import create_engine
import os

db_url = f"postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@db:5432/{os.getenv("POSTGRES_DB")}"

engine = create_engine(db_url, echo=True)