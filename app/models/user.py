from sqlalchemy import Boolean, Column, String
from sqlalchemy.dialects.mysql import INTEGER
from app.db.session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(INTEGER, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return "유저 정보는 '%s', '%s'" % (
            self.id, self.email
        )
