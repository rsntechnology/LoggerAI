# main.py
from fastapi import FastAPI
from adapters.webhook_adapter import router as webhook_router
from adapters.data_adapter import router as data_router
from application.core.repositories import DataRepository
from os.path import join, dirname

app = FastAPI()


# Include routers in the main application
app.include_router(webhook_router, prefix="/webhook")
app.include_router(data_router, prefix="/data")
