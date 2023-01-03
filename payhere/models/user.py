from sqlalchemy import Boolean, Column, String
from sqlalchemy.dialects.mysql import INTEGER
from payhere.db.session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(INTEGER, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))

    def __repr__(self):
        return "유저 정보는 '%s', '%s'" % (
            self.id, self.email
        )
