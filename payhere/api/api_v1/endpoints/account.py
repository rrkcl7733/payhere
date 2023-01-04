from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from payhere.db.session import Base, engine, get_db
from payhere.api.depends import get_current_user
from payhere.schemas.account import AccountCreate, AccountUpdate, AccountList
from payhere.models.user import User
from payhere.models.account import Account

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create(acc: AccountCreate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_acc = Account(
        user_id=user.id,
        money=acc.money,
        memo=acc.memo
    )
    db.add(db_acc)
    db.commit()
    db.refresh(db_acc)


@router.put("/{account_id}", status_code=status.HTTP_200_OK)
def update(account_id: int, acc: AccountUpdate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_update = db.query(Account).filter(Account.id == account_id, user.id == Account.user_id).first()
    if not db_update:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="없는 가계부이거나 권한 없음",
        )
    db_update.money = acc.money
    db_update.memo = acc.memo
    db.add(db_update)
    db.commit()
    db.refresh(db_update)


@router.delete("/{account_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(account_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_delete = db.query(Account).filter(Account.id == account_id, user.id == Account.user_id).first()
    if not db_delete:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="없는 가계부이거나 권한 없음",
        )
    db.delete(db_delete)
    db.commit()


@router.get("/show", response_model=list[AccountList], status_code=status.HTTP_200_OK)
def show(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Account).filter(Account.user_id == user.id).all()