from AlcMan import AlchemyManager



if __name__ == '__main__':
    m = AlchemyManager(db_type='postgresql', db_lib='psycopg2',
                       login='postgres',
                       password='1111', db_name='test')
    # m.create_table()
    # m.insert_data()
    print(m.select_data(3))
    # m.delete_data(4)
    # m.drop_tables()



