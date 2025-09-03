from fastapi import FastAPI
from app.api.main import api_router

app = FastAPI()

@app.get("/health")
async def root():
    return {"message": "Healthy :-)"}

app.include_router(api_router)