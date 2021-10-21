import psycopg2
from psycopg2 import Error
import typing


class SQLManager:
    def __init__(self, dbname, db_user, password, hostname):
        self.dbname = dbname
        self.user = db_user
        self.password = password
        self.host = hostname
        self.conn = psycopg2.connect(user=self.user,
                                     password=self.password,
                                     host=self.host, database=self.dbname)
        self.cur = self.conn.cursor()

    # CREATE METHOD

    def create_table(self):
        self.cur.execute("""
                    CREATE TABLE IF NOT EXISTS Shops(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100),
                        address TEXT NULL,
                        staff_amount INT CHECK (staff_amount > -1)
                    ); 
                    CREATE TABLE IF NOT EXISTS Departments(
                        id SERIAL PRIMARY KEY ,
                        sphere VARCHAR(100),
                        staff_amount INT CHECK (staff_amount > -1),
                        shop_id INT,
                        FOREIGN KEY (shop_id) REFERENCES Shops(id)
                    );
                    CREATE TABLE IF NOT EXISTS Items(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100),
                        description TEXT NULL,
                        price DECIMAL(50,3) CHECK (price > -1),
                        department_id INT,
                        FOREIGN KEY (department_id) REFERENCES Departments(id)
                    );
                     """)
        self.cur.commit()

    # INSERT METHOD

    def insert_data(self):
        query_insert_into_shops = """
        INSERT INTO Shops(name, address, staff_amount) 
        VALUES (%s,%s,%s);
        """
        shops_data = (
            ('Auchan', None, 250),
            ('IKEA', 'Street Žirnių g. 56, Vilnius, Lithuania.', 500),
        )
        self.cur.executemany(query_insert_into_shops, shops_data)
        self.cur.commit()

        query_insert_into_departments = """
                INSERT INTO Departments(sphere, staff_amount, shop_id) 
                VALUES (%s,%s,%s);
            """
        departments_data = (
            ('Furniture', 250, 1),
            ('Furniture', 300, 2),
            ('Dishes', 200, 2)
        )
        self.cur.executemany(query_insert_into_departments, departments_data)
        self.cur.commit()

        query_insert_into_items = """
                INSERT INTO Items(name, description, price, department_id) 
                VALUES (%s,%s,%s,%s);
            """
        items_data = (
            ('Table', 'Cheap wooden table', 300, 1),
            ('Table', None, 750, 2),
            ('Bed', 'Amazing wooden bed', 1200, 2),
            ('Cup', None, 10, 3),
            ('Plate', 'Glass plate', 20, 3),
        )
        self.cur.executemany(items_data)
        self.cur.commit()

    def select_data(self, choice: typing.Optional[int]):
        data = None
        select_query = [
            """SELECT * FROM Items WHERE description IS NOT NULL;""",
            """SELECT DISTINCT sphere FROM Departments 
            WHERE staff_amount > 200;""",
            """SELECT address FROM Shops WHERE name ILIKE 'i%';""",
            """
                SELECT Items.name FROM Items
                INNER JOIN Departments ON Departments.id = Items.department_id
                WHERE Departments.sphere = 'Furniture';
            """,
            """
                SELECT Shops.name FROM Shops
                INNER JOIN Departments ON Departments.shop_id = Shops.id
                INNER JOIN Items ON Items.department_id = Departments.id
                WHERE Items.description IS NOT NULL;
            """,
            """
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
            """,
            """
                SELECT id FROM Items
                ORDER BY name
                LIMIT 2
                OFFSET 3;
            """,
            """
                SELECT Items.name, Departments.id FROM Items
                INNER JOIN Departments ON Items.department_id = Departments.id;
            """,#
            """
                SELECT Items.name, Departments.id FROM Items
                LEFT JOIN Departments ON Items.department_id = Departments.id
            """,#
            """
                SELECT Items.name, Departments.id FROM Items
                RIGHT JOIN Departments ON Items.department_id = Departments.id
            """,#
            """
                SELECT Items.name, Departments.id FROM Items
                FULL JOIN Departments ON Items.department_id = Departments.id
            """,#
            """
                SELECT Items.name, Departments.id FROM Items
                CROSS JOIN Departments;
            """,#
            """
                SELECT Shops.name, COUNT(*) as count_goods, SUM(price),
                MAX(price), MIN(price),
                AVG(price) FROM Items
                INNER JOIN Departments ON Departments.id = Items.department_id
                INNER JOIN Shops ON Shops.id = Departments.shop_id
                GROUP BY (Shops.name)
                HAVING count_goods > 1;
            """,#
            """
                SELECT Shops.name, ARRAY[i.name, i.description, i.price::text]
                FROM Shops s
                LEFT JOIN Departments d ON d.shop_id = s.id
                LEFT JOIN Items i ON i.department_id = d.id; 
                
            """,
        ]
        with self.conn.cursor() as curs:
            if choice in range(1, 15):
                curs.execute(select_query[choice - 1])
                if choice == 14:
                    new_data = curs.fetchall()
                    data = {}
                    for el in new_data:
                        data.setdefault(el[0], []).append(el[1])
                else:
                    curs.execute(select_query[choice - 1])
                    data = curs.fetchall()
        return data

    # UPDATE METHOD

    def update_data(self):
        self.cur.execute("""
            UPDATE Items SET price = price + 100 
            WHERE name ILIKE 'b%' OR name ILIKE '%e'; 
        """)
        self.cur.commit()

    # DELETE METHODS

    def delete_data(self, choice: typing.Optional[int]):
        delete_query = [
            """DELETE FROM Items WHERE price > 500 AND description IS NULL;""",
            """DELETE FROM Items WHERE id IN 
            (
                SELECT Items.id FROM Items
                INNER JOIN Departments ON Departments.id = Items.department_id
                INNER JOIN Shops ON Shops.id = department_id
                WHERE Shops.address is NULL
            )""",
            """
                DELETE FROM Items
                WHERE Items.id IN (
                    SELECT id FROM Departments
                    WHERE staff_amount < 225 
                    OR staff_amount > 275
                );
            """,
            """
                TRUNCATE TABLE Shops CASCADE;
                TRUNCATE TABLE Departments CASCADE;
                TRUNCATE TABLE Items CASCADE;
            """
        ]
        with self.conn.cursor() as curs:
            if choice in range(1, 5):
                self.cur.execute(delete_query[choice - 1])

    # DROP METHOD

    def drop_table(self):
        self.cur.execute("""DROP TABLE IF EXISTS Shops CASCADE ;""")
        self.cur.execute("""DROP TABLE IF EXISTS Departments CASCADE;""")
        self.cur.execute("""DROP TABLE IF EXISTS Items CASCADE;""")
        self.cur.commit()
