from fastapi import FastAPI

from payhere.api.api import api_router
from payhere.core.config import settings
from payhere.db.session import SessionLocal


app = FastAPI()
app.include_router(api_router, prefix=settings.API_V1_STR)