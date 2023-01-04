from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

from payhere.db.session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(INTEGER, primary_key=True, index=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))

    accounts = relationship("Account", back_populates="users")

    def __repr__(self):
        return "유저 정보는 '%s', '%s'" % (
            self.id, self.email
        )
