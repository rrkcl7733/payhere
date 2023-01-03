from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from payhere.core.config import settings
from payhere.core.security import create_access_token
from payhere.db.session import Base, engine, get_db
from payhere.schemas.user import UserCreate

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.post("/register")
def post(user: UserCreate, db: Session = Depends(get_db)):
