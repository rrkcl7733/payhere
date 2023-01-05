from sqlalchemy import Column, String, ForeignKey, DATETIME
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

from payhere.db.session import Base


class Account(Base):
    __tablename__ = 'account'

    id = Column(INTEGER, primary_key=True, index=True, autoincrement=True)
    user_id = Column(INTEGER, ForeignKey("user.id"))
    money = Column(INTEGER)
    memo = Column(String(255))
    share = Column(DATETIME)

    users = relationship("User", back_populates="accounts")

    def __repr__(self):
        return "가계부 정보는 ('%s', '%s'), '%s', '%s'" % (
            self.id, self.user_id, self.money, self.memo
        )