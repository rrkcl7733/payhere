from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm

from payhere.core.config import settings
from payhere.core.security import create_access_token
from payhere.db.session import Base, engine, get_db
from payhere.schemas.user import UserCreate
from payhere.models.user import User
from payhere.core.security import get_password_hash, verify_password

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.post("/register")
def post(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="등록된 이메일입니다")
    db_obj = User(
        email=user.username,
        password=get_password_hash(user.password)
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    del db_obj.password


@router.post("/login")
async def login_for_access_token(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="없는 이메일이거나 비밀번호 다름",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(subject=db_user.email, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get('/logout')
async def logout(req: Request):
    # request 에서 header에 토큰 삭제방법 없음
    return req
