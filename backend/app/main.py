from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import os

from .models.database import create_db_and_tables
from .api.api import api_router
from .auth.auth import auth_router

app = FastAPI(
    title="Buddie API",
    description="Cannabis concierge API",
    version="0.1.0"
)

# Set up CORS
origins = [
    "http://localhost:3000",  # Local frontend
    "https://buddie.fly.dev",  # Production frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/auth")

@app.on_event("startup")
async def on_startup():
    create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Welcome to Buddie API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 