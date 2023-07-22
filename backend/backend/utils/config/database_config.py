from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class PostgresSettings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_port: int

    model_config = SettingsConfigDict(env_file=os.path.join(
        os.path.dirname(__file__),'.env'))
