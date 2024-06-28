from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = Field(default='sqlite+asyncpg://workout:workout@localhost/workout')


settings = Settings()