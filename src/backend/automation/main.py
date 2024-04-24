from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI()


# Include API routes
app.include_router(api_router)
