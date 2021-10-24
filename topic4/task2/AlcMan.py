from sqlalchemy import Column, MetaData, Integer, String, Text, ForeignKey, \
    update, insert, text, and_, or_
from sqlalchemy.orm import Session, sessionmaker
from models.Items import Items
from models.Shops import Shops
from models.Departments import Departments
from base import Base
from sqlalchemy.future import create_engine
from sqlalchemy.sql import func
import typing


class AlchemyManager:
    def __init__(self, db_type: typing.Optional[str],
                 db_lib: typing.Optional[str], login: typing.Optional[str],
                 password: typing.Optional[str], db_name: typing.Optional[str],
                 host: typing.Optional[str] = '127.0.0.1') -> 'self':
        # PARAMS
        self.host = host
        self.db_name = db_name
        self.password = password
        self.login = login
        self.db_lib = db_lib
        self.db_type = db_type

        # ENGINE
        self.engine = create_engine(
            f'postgresql+psycopg2://postgres:1111@127.0.0.1/test',
            echo=False
        )
        # self.engine = sqlalchemy.create_engine(
        #     f'{self.db_type}+{self.db_lib}://{self.login}:{self.password}@{self.host}/{self.db_name}',
        #     echo=True,
        # )

        # self.engine = create_engine(
        #     f'sqlite:///test.db')
        self.session = Session(bind=self.engine, future=True)

    # CREATE METHODS
    def create_table(self):
        """Create tables"""
        Base.metadata.create_all(self.engine)

    # INSERT METHODS
    def insert_data(self):
        """Insert data into DB"""
        data_insert = [
            Shops(
                name='Auchan',
                address=None,
                staff_amount=250,
            ),
            Shops(
                name='IKEA',
                address='Street Žirnių g. 56, Vilnius, Lithuania.',
                staff_amount=500,
            ),
            Departments(
                sphere='Furniture',
                staff_amount=250,
                shop_id=1,
            ),
            Departments(
                sphere='Furniture',
                staff_amount=300,
                shop_id=2,
            ),
            Departments(
                sphere='Dishes',
                staff_amount=200,
                shop_id=2,
            ), Items(
                name='Table',
                description='Cheap wooden table',
                price=300,
                department_id=1,
            ),
            Items(
                name='Table',
                description=None,
                price=750,
                department_id=2,
            ),
            Items(
                name='Bed',
                description='Amazing wooden bed',
                price=1200,
                department_id=2,
            ),
            Items(
                name='Cup',
                description=None,
                price=10,
                department_id=3,
            ),
            Items(
                name='Plate',
                description='Glass plate',
                price=20,
                department_id=3,
            ),
        ]
        with self.session.begin() as session:
            session.session.add_all(data_insert)

    # SELECT METHODS
    def select_data(self, choice: typing.Optional[int]):
        # eval with string, idea to use dict
        data = None
        query_dict = [
            #1
            lambda x: x.query(Items).filter(
                Items.description.is_not(None)
            ).all(),
            #2
            lambda x: [y.sphere for y in x.query(Departments).filter(
                Departments.staff_amount > 200).distinct(Departments.sphere)],
            #3
            lambda x: [y.address for y in x.query(Shops).filter(
                Shops.name.ilike('i%'))],
            #4
            lambda x: [y for y in x.query(Items).join(
                Departments, Departments.id == Items.department_id).filter(
                Departments.sphere == 'Furniture'
            )],
            #5
            lambda x: [y for y in x.query(Shops).join(
                Departments, Departments.shop_id == Shops.id
            ).join(
                Items, Departments.id == Items.department_id
            ).filter(
                Items.description.is_not(None))],
            #6
            lambda x: x.query(Items, Departments, Shops).outerjoin(
                Departments, Departments.id == Items.department_id
            ).outerjoin(
                Shops, Shops.id == Departments.shop_id
            ).all(),
            #7
            lambda x: x.query(Items).order_by(
                Items.name).limit(2).offset(3).all(),
            #8
            lambda x: x.query(Items, Departments).join(
                Departments, Departments.id == Items.department_id
            ).all(),
            #9
            lambda x: x.query(Items, Departments).outerjoin(
                Departments, Departments.id == Items.department_id
            ).all(),
            #10
            lambda x: x.query(Items, Departments).join(
                Items, Items.department_id == Departments.id,
                isouter=True
            ).all(),
            #11
            lambda x: x.query(Items, Departments).join(
                Departments, full=True
            ).all(),
            #12
            lambda x: x.query(Items, Departments).all(),
            #13
            lambda x: self.session.query(
                # Shops.name,
                func.count('*').label('count_goods'),
                func.sum(Items.price),
                func.max(Items.price),
                func.min(Items.price),
                func.avg(Items.price),
            ).join(
                Departments, Departments.id == Items.department_id
            ).join(
                Shops, Shops.id == Departments.shop_id
            ).group_by(Shops.name).having(func.count('*') > 1).all(),
            #14
            lambda x: [y for y in x.query(Shops, x.query(Items).join(
                Departments
                ).join(Shops)
                )
                ]
        ]
        if choice in range(1, 15):
            data = query_dict[choice - 1](self.session)
            print(data)
            for row in data:
                print(row.name)
        return query_dict[choice - 1](self.session)

    # DELETE METHODS
    def delete_data(self, choice: typing.Optional[int]):
        """Delete data form DB in tables Items, Departments, Shops"""
        delete_query = [
            lambda x: x.query(Items).where(
                and_(Items.price > 500, Items.description.is_(None))
            ),
            lambda x: x.query(Items).where(
                and_(
                        Departments.id == Items.department_id,
                        Shops.id == Departments.shop_id,
                        Shops.address.is_(None)
                )
            ),
            lambda x: x.query(Items).where(
                and_(
                    Items.department_id == Departments.id,
                    or_(
                        Departments.staff_amount < 225,
                        Departments.staff_amount > 275
                    )
                )
            ),
            # ? how to truncate table
            # lambda x: x.execute(table.delete()) for table in Base.metadata.sorted_tables
        ]
        if choice in range(1, 4):
            with self.session.begin() as session:
                delete_query[choice - 1](self.session).delete(
                    synchronize_session=False
                )

    # DROP METHOD
    def drop_tables(self):
        """Drop tables"""
        Base.metadata.drop_all(bind=self.engine)



