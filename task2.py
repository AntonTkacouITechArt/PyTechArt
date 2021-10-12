from sqlalchemy import Column, MetaData, Integer, String, Text, ForeignKey, \
    update, insert, relationship, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, Session, sessionmaker
from Items import Items
from Shops import Shops
from Departments import Departments

if __name__ == '__main__':
    # connections
    engine = sqlalchemy.create_engine(
        'postgresql+psycopg2://postgres:1111@127.0.0.1/test',
        echo=True,
    )
    print(engine)
    Session = sessionmaker(bind=egine)
    session = Session()

    # creating Tables
    Base = declarative_base()

    Base.metadata.create_all(engine)

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

    session.add_all(shops_data_insert)
    session.commit()
    session.add_all(departments_data_insert)
    session.commit()
    session.add_all(items_data_insert)
    session.commit()

    # select data
    select1 = session.query(Items).filter(text("description is not NULL")).all()
    select2 = session.query(Departments.sphere).from_statement(
        text("SELECT DISTINCT * FROM Departments WHERE staff_amount > 200;")
    ).all()
    select3 = session.query(Shops.address).from_statement(
        text("SELECT * FROM Shops WHERE name ~ '^(I|i)';")
    ).all()
    select4 = session.query(Items.name).from_statement(
        text("""
        SELECT Items.name FROM Items
        INNER JOIN Departments ON Departments.id = Items.department_id
        WHERE Departments.sphere = 'Furniture';""")
    ).all()
    select5 = session.query(Shops.name).from_statement(

    )

    # delete from tables
    # 1 check
    del1 = session.query(Items).filter(
        and_(Items.price > 500, Items.description is None)
    ).all()
    session.delete(del1)
    session.commit()
    # 2 check
    del2 = session.query(Items).filter(
        Items.departments.shops.address is None
    ).all()
    session.delete(del2)
    session.commit()
    # 3 check
    del3 = session.query(Items).filter(
        text(
            'id IN [(SELECT id FROM department WHERE staff_amount < 225 OR staff_amount > 275)]')
    ).all()
    session.delete(del3)
    session.commit()
    # 4
    session.execute('''TRUNCATE TABLE shops''')
    session.commit()
    session.execute('''TRUNCATE TABLE departments''')
    session.commit()
    session.execute('''TRUNCATE TABLE items''')
    session.commit()

    # drop tables
    Base.metadata.drop_all(engine)
    session.close()
