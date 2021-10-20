from AlcMan import AlchemyManager



if __name__ == '__main__':
    m = AlchemyManager(db_type='postgresql', db_lib='psycopg2',
                       login='postgres',
                       password='1111', db_name='test')
    # m.create_table()
    # m.insert_data()
    # m.drop_tables()
    m.delete_data(1)
    # print(m.select_data(5))

    # f'postgresql+psycopg2://postgres:1111@127.0.0.1/test',