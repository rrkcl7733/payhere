from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from payhere.api.api import api_router
from payhere.core.config import settings


app = FastAPI()
app.include_router(api_router, prefix=settings.API_V1_STR)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[f"http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)