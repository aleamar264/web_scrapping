from ..utils.config import database_config

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..utils.get_eth0 import get_interface_ip

def settings():
    return database_config.PostgresSettings().model_dump()

interface_name = "eth0"
ip_address = get_interface_ip(interface_name)

class CreateConnection:
    def __init__(self) -> None:
        __settings = settings()
        SQLALCHEMY_DATABASE_URL=\
            f"""postgresql+psycopg2://{__settings['postgres_user']}:{__settings['postgres_password']}@db:{__settings['postgres_port']}/{__settings['postgres_db']}"""
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL)
        self.__SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.__Base = declarative_base()
    
    @property
    def get_base(self):
        return self.__Base

    @property
    def get_SessionLocal(self):
        return self.__SessionLocal()
    
    @property
    def get_engine(self):
        return self.engine
