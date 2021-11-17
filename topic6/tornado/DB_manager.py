import typing
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.base import Base


class Manager:
    def __init__(self, db_user: str, db_password: str, db_host: str,
                 db_name: str):
        self.engine = create_engine(
            f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}/{db_name}',
            echo=True,
        )
        self.session = Session(bind=self.engine, future=True)

    def create_tables(self) -> None:
        """Create table"""
        Base.metadata.create_all(self.engine)

manager = None

def connect_db(db_user: str, db_password: str, db_host: str,
               db_name: str) -> None:
    """Connect to DB"""
    global manager
    manager = Manager(db_user, db_password, db_host, db_name)
    manager.create_tables()
