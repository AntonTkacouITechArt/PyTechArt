from sqlalchemy import Column, MetaData, Integer, String, Text, ForeignKey, \
    update, insert, text, and_, or_
from sqlalchemy.orm import Session, sessionmaker
from models.Items import Items
from models.Shops import Shops
from models.Departments import Departments
from base import Base
from sqlalchemy.future import create_engine
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
            echo=True
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
            self.session.query(Items).filter(
                text("description is not NULL")).all(),
            self.session.query(Departments.sphere).distinct(
                Departments.sphere).filter(Departments.staff_amount > 200
                                           ).all(),
        #     # self.session.query(Shops.address).from_statement(
        #     #     text("SELECT * FROM Shops WHERE name ~ '^(I|i)';")
        #     # ).all(),
            self.session.query(Items.name).join(
                Departments, Departments.id == Items.department_id).filter(
                Departments.sphere == 'Furniture'
            ).all(),
        #     self.session.query(
        #         Shops.name).join(
        #         Departments, Departments.shop_id == Shops.id).join(
        #         Items, Departments.id == Items.department_id).filter(
        #         Items.description is not None).all(),
        #     self.session.query(Items, Departments, Shops).from_statement(
        #         text("""
        #     SELECT
        #         Items.name, description, price,
        #         'department_' || sphere AS dep_sphere,
        #         'department_' || Departments.staff_amount AS dep_staff,
        #         'shop_' || Shops.name AS shop_name,
        #         'shop_' || address AS shop_addr,
        #         'shop_' || Shops.staff_amount as shop_staff
        #     FROM Items
        #     INNER JOIN Departments ON Departments.id = Items.department_id
        #     INNER JOIN Shops ON Shops.id = Departments.shop_id;
        # """)
        #     ).all(),
            self.session.query(Items.id).order_by(Items.name).limit(
                2).offset(3).all(),
            self.session.query(Items.name, Departments.id).join(
                Departments, Departments.id == Items.department_id).all(),
        #     self.session.query(Items.name, Departments.id).outerjoin(
        #         Departments, Departments.id == Items.department_id).all(),
        #     # 10: self.session.query()
        ]
        if choice in range(1, 15):
            data = query_dict[choice - 1]
            for row in data:
                print(row)
            # data = self.session.query(Items).filter(
            #         text("description is not NULL")).all()
            # for row in data:
            #     print("Name: ", row.name, "Address:", row.description, "Email:",
            #           row.price)
        return data

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
                or_(Departments.staff_amount < 225,
                Departments.staff_amount > 275)
                )
            ),
            # lambda x: x.execute(table.delete()) for table in Base.metadata.sorted_tables
        ]
        if choice in range(1, 4):
            with self.session.begin() as session:
                delete_query[choice - 1](self.session).delete(
                    synchronize_session=False
                )

    def drop_tables(self):
        """Drop tables"""
        Base.metadata.drop_all(bind=self.engine)


