from fastapi import FastAPI
from .database import engine
from . import models
# from .routers import ledger, stock

# Create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# # Include routers
# app.include_router(ledger.router, prefix="/ledger", tags=["Ledger"])
# app.include_router(stock.router, prefix="/stock", tags=["Stock"])

@app.get("/")
def root():
    return {"message": "Welcome to the Ledger System FastAPI project!"}