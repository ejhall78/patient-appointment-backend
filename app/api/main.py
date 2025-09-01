from fastapi import APIRouter

from app.api.routes import patients

api_router = APIRouter()
api_router.include_router(patients.router)