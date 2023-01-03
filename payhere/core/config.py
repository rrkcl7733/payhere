import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    HOST: str = os.getenv('HOST')
    PORT: str = os.getenv('PORT')
    USERNAME: str = os.getenv('NAME')
    PASSWORD: str = os.getenv('PASSWORD')
    DATABASE: str = os.getenv('DATABASE')
    SQLALCHEMY_DATABASE_URL = f'mysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

    class Config:
        case_sensitive = True


settings = Settings()