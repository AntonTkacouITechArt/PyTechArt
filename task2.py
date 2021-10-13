from sqlalchemy import Column, MetaData, Integer, String, Text, ForeignKey, \
    update, insert, relationship, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, Session, sessionmaker
from Items import Items
from Shops import Shops
from Departments import Departments


# question with model in another file
# how to use table

class AlchemyManager:
    def __init__(self, db_type, db_lib, login, password, db_name,
                 port='127.0.0.1'):
        # params
        self.port = port
        self.db_name = db_name
        self.password = password
        self.login = login
        self.db_lib = db_lib
        self.db_type = db_type

        # engine
        self.engine = sqlalchemy.create_engine(
            f'postgresql+psycopg2://postgres:1111@127.0.0.1/test',
            echo=True,
        )
        self.Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.commit = self.session.commit()

    # how to crete table in another file
    def create_table(self):
        # sqlalchemy
        Base = declarative_base()
        Base.metadata.create_all(engine)

        pass

    # INSERT METHODS
    def insert_all_data(self, data):
        self.session.add_all(data)
        self.commit()

    def insert_one_data(self, data):
        self.session.add(data)
        self.commit()

    # SELECT METHODS
    def select_1(self):
        return self.session.query(Items).filter(
            text("description is not NULL")).all()

    def select_2(self):
        return self.session.query(Departments.sphere).distinct(
            Departments.sphere).all()

    def select_3(self):
        return self.session.query(Shops.address).from_statement(
            text("SELECT * FROM Shops WHERE name ~ '^(I|i)';")
        ).all()

    def select_4(self):
        return self.session.query(Items.name).join(Items.departments).filter(
            Departments.sphere == 'Furniture'
        ).all()

    def select_5(self):
        return self.session.query(
            Shops.name).join(Departments, Shops.id).join(
            Items, Departments.id).filter(Ite.description is not None)

    def select_6(self):
        return self.session.query(Items, Departments, Shops).from_statement(
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
        ).all()

    def select_7(self):
        return self.session.query(Items.id).order_by(Items.name).limit(2).offset(3)
    
    def select_8(self):
        return self.session.query(Items.name, Departments.id)



    # DELETE METHODS
    def delete_1(self):
        # how to use model !!!!
        del1 = self.session.query(Items).filter(
            and_(Items.price > 500, Items.description is None)
        ).all()
        self.session.delete(del1)
        self.commit()

    def delete_2(self):
        del2 = self.session.query(Items).filter(
            Items.departments.shops.address is None
        ).all()
        self.session.delete(del2)
        self.commit()

    def delete_3(self):
        del3 = self.session.query(Items).filter(
            text(
                'id IN (SELECT id FROM department WHERE staff_amount < 225 OR staff_amount > 275);')
        ).all()
        self.session.delete(del3)
        self.commit()

    def delete_4(self):
        self.session.execute('''TRUNCATE TABLE shops''')
        self.commit()
        self.session.execute('''TRUNCATE TABLE departments''')
        self.commit()
        self.session.execute('''TRUNCATE TABLE items''')
        self.commit()

    def drop_tables(self):
        Base.metadata.drop_all(engine)

    def close_session(self):
        self.session.close()


if __name__ == '__main__':
    # connections
    sqlmanager = AlchemyManager('postgresql', 'psycopg2', 'postgres', '1111',
                                'test')
    print(sqlmanager.engine)

    # creating Tables

    # insert data
    shops_data_insert = [
        Shops(
            name='Auchan',
            address=None,
            staff_amount=250,
        ),
        Shops(
            name='IKEA',
            address='Street Žirnių g. 56, Vilnius, Lithuania.',
            staff_amount=500,
        )
    ]
    departments_data_insert = [
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
        ),
    ]
    items_data_insert = [
        Items(
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

    sqlmanager.insert_all_data(shops_data_insert)
    sqlmanager.insert_all_data(departments_data_insert)
    sqlmanager.insert_all_data(items_data_insert)

    # select data


    select5 = session.query(Shops.name).from_statement(

    )

    # delete talbes
    sqlmanager.delete_1()
    sqlmanager.delete_2()
    sqlmanager.delete_3()
    sqlmanager.delete_4()

    # drop tables
    sqlmanager.drop_tables()

    sqlmanager.close_session()
