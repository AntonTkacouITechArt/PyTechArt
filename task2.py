from sqlalchemy import Column, MetaData, Integer, String, Text, ForeignKey,



if __name__ == '__main__':
    engine = sqlalchemy.create_engine(
        'postgresql+psycopg2://postgres:1111@127.0.0.1/test',
        echo=True,
    )

    engine.connect()

    print(engine)
    metadata = MetaData()

    shops = sqlalchemy.Table(
        'shops', metadata,
        Column('id', Integer(), primary_key=True),
        Column('name', String(100), nullable=False),
        Column('address', Text(), ),
        Column('staff_amount', Integer()),
        CheckConstraint('staff_amount > -1', name='shops_staff_amount_check'),
    )

    departments = sqlalchemy.Table(
        'departments', metadata,
        Column('id', Integer(), primary_key=True),
        Column('sphere', String(100), nullable=False),
        Column('staff_amount', Integer()),
        CheckConstraint('staff_amount > -1', name='departments_staff_amount_check'),
        Column('shop_id', ForeignKey('shops.id')),
    )

    items = sqlalchemy.Table(
        'items', metadata,
        Column('id', Integer(), primary_key=True),
        Column('name', String(100), nullable=False),
        Column('description', Text()),
        Column('price', Numeric(50,3)),
        Column('department_id', ForeignKey('departments.id')),
        CheckConstraint('price > -1', name='items_price_check'),
    )

    MetaData.create_all(engine)