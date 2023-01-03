from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from payhere.core.config import settings
from payhere.core.security import create_access_token
from payhere.db.session import Base, engine, get_db
from payhere.schemas.user import UserCreate
from payhere.models.user import User
from payhere.core.security import get_password_hash

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.post("/register")
def post(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status=400, detail="등록된 이메일입니다")
    db_obj = User(
        email=user.email,
        password=get_password_hash(user.password)
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    del db_obj.password