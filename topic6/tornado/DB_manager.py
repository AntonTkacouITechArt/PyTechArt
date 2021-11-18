from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

engine = create_engine('postgresql+psycopg2://postgres:1111@127.0.0.1/test2',
                       echo=False)

Session = sessionmaker(bind=engine)


def create_tables() -> None:
    Base.metadata.create_all(engine)
