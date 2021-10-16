from sqlalchemy import Column, MetaData, Integer, String, Text, ForeignKey, \
    update, insert, relationship, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, Session, sessionmaker
from Items import Items
from Shops import Shops
from Departments import Departments
import typing


# question with model in another file
# how to use table

class AlchemyManager:
    def __init__(self, db_type: typing.Optional[str],
                 db_lib: typing.Optional[str], login: typing.Optional[str],
                 password: typing.Optional[str], db_name: typing.Optional[str],
                 host: typing.Optional[str] = '127.0.0.1') -> self:
        # params
        self.host = host
        self.db_name = db_name
        self.password = password
        self.login = login
        self.db_lib = db_lib
        self.db_type = db_type

        # engine
        # self.engine = sqlalchemy.create_engine(
        #     f'postgresql+psycopg2://postgres:1111@127.0.0.1/test',
        #     echo=True,
        # )
        self.engine = sqlalchemy.create_engine(
            f'{self.db_type}+{self.db_lib}://{self.login}:{self.password}@{self.host}/{self.db_name}',
            echo=True,
        )
        self.Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.commit = self.session.commit()

    # how to crete table in another file
    # CREATE METHODS
    def create_table(self):
        # sqlalchemy
        Base = declarative_base()
        Base.metadata.create_all(engine)

    # INSERT METHODS
    def insert_data(self):
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
        self.session.add_all(data_insert)
        self.commit()

    # SELECT METHODS
    def select_data(self, choice: typing.Optional[int]):
        # eval with string, idea to use dict
        data = None
        query_dict = {
            1: self.session.query(Items).filter(
                text("description is not NULL")).all(),
            2: self.session.query(Departments.sphere).distinct(
                Departments.sphere).filter(Departments.staff_amount > 200
                                           ).all(),
            3: self.session.query(Shops.address).from_statement(
                text("SELECT * FROM Shops WHERE name ~ '^(I|i)';")
            ).all(),
            4: self.session.query(Items.name).join(
                Departments, Departments.id == Items.department_id).filter(
                Departments.sphere == 'Furniture'
            ).all(),
            5: self.session.query(
                Shops.name).join(
                Departments, Departments.shop_id == Shops.id).join(
                Items, Departments.id == Items.department_id).filter(
                Items.description is not None).all(),
            6: self.session.query(Items, Departments, Shops).from_statement(
                text("""
            SELECT 
                Items.name, description, price,
                'department_' || sphere AS dep_sphere,
                'department_' || Departments.staff_amount AS dep_staff,
                'shop_' || Shops.name AS shop_name,
                'shop_' || address AS shop_addr, 
                'shop_' || Shops.staff_amount as shop_staff
            FROM Items
            INNER JOIN Departments ON Departments.id = Items.department_id
            INNER JOIN Shops ON Shops.id = Departments.shop_id;
        """)
            ).all(),
            7: self.session.query(Items.id).order_by(Items.name).limit(
                2).offset(3).all(),
            8: self.session.query(Items.name, Departments.id).join(
                Departments, Departments.id == Items.department_id).all(),
            9: self.session.query(Items.name, Departments.id).outerjoin(
                Departments, Departments.id == Items.department_id).all(),
            # 10: self.session.query()
        }
        if choice in range(1, 15):
            data = query_dict[choice - 1]
        return data

    # DELETE METHODS
    def delete_data(self, choice: typing.Optional[int]):
        # eval with string, idea to use dict
        # how to use model !!!!
        # rewrite query 4
        query_dict = {
            1: self.session.query(Items).filter(
                and_(Items.price > 500, Items.description is None)
            ).all(),
            2: self.session.query(Items).filter(
                Items.departments.shops.address is None
            ).all(),
            3: self.session.query(Items).filter(
                text(
                    """id IN (SELECT id FROM department 
                    WHERE staff_amount < 225 OR staff_amount > 275);""")
            ).all(),
            4: self.session.execute('''
        TRUNCATE TABLE shops CASCADE;
        TRUNCATE TABLE departments CASCADE;
        TRUNCATE TABLE items CASCADE;
        '''),
        }
        if choice in range(1, 4):
            self.session.delete(query_dict[choice - 1])
            self.commit()

    def drop_tables(self):
        Base.metadata.drop_all(bind=self.engine)



if __name__ == '__main__':
    m = AlchemyManager(db_type='postgresql', db_lib='psycopg2',login='postgres',
                       password='1111',db_name='test')
    m.create_table()
    # f'postgresql+psycopg2://postgres:1111@127.0.0.1/test',
