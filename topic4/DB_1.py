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
            ('Furniture', 300, 2)
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


    def select_data(self, choice:typing.Optional[int]):
        if choice == 1:
            self.cur.execute("""
                        SELECT * FROM Items
                        WHERE description IS NOT NULL;
                    """)
            data = self.cur.fetchall()
            return data
        elif choice == 2:
            self.cur.execute("""
                                SELECT DISTINCT sphere FROM Departments
                                WHERE staff_amount > 200;
                            """)
            data = self.cur.fetchall()
            return data
        elif choice == 3:
            self.cur.execute("""
                        SELECT address FROM Shops
                        WHERE name ~ '^(I|i)';
                    """)
            data = self.cur.fetchall()
            return data
        elif choice == 4:
            self.cur.execute("""
                        SELECT Items.name FROM Items
                        INNER JOIN Departments ON Departments.id = Items.department_id
                        WHERE Departments.sphere = 'Furniture';
                    """)
            data = self.cur.fetchall()
            return data
        elif choice == 5:
            self.cur.execute("""
                        SELECT Shops.name FROM Shops
                        INNER JOIN Departments ON Departments.shop_id = Shops.id
                        INNER JOIN Items ON Items.department_id = Departments.id
                        WHERE Items.description IS NOT NULL;
                    """)
            data = self.cur.fetchall()
            return data
        elif choice == 6:
            self.cur.execute("""
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
            data = self.cur.fetchall()
            return data
        elif choice == 7:
            self.cur.execute("""
                        SELECT id FROM Items
                        ORDER BY name
                        LIMIT 2
                        OFFSET 3;
                    """)
            data = self.cur.fetchall()
            return data
        elif choice == 8:
            self.cur.execute("""
                                SELECT Items.name, Shops.name FROM Items
                                INNER JOIN Departments ON Items.department_id = Departments.id
                                INNER JOIN Shops ON Shops.id = Departments.shop_id;
                            """)
            data = self.cur.fetchall()
            return data
        elif choice == 9:
            self.cur.execute("""
                                SELECT Items.name, Departments.id FROM Items
                                LEFT JOIN Departments ON Items.department_id = Departments.id
                        """)
            data = self.cur.fetchall()
            return data
        elif choice == 10:
            self.cur.execute("""
                                SELECT Items.name, Departments.id FROM Items
                                RIGHT JOIN Departments ON Items.department_id = Departments.id
                            """)
            data = self.cur.fetchall()
            return data
        elif choice == 11:
            self.cur.execute("""
                                SELECT Items.name, Departments.id FROM Items
                                FULL JOIN Departments ON Items.department_id = Departments.id
                        """)
            data = self.cur.fetchall()
            return data
        elif choice == 12:
            self.cur.execute("""
                                SELECT Items.name, Shops.name FROM Items
                                CROSS JOIN Departments
                                INNER JOIN Shops ON Shops.id = Departments.shop_id;
                        """)
            data = self.cur.fetchall()
            return data
        elif choice == 13:
            self.cur.execute("""
                    SELECT Shops.name, COUNT(*) as count_goods, SUM(price),
                    MAX(price), MIN(price),
                    AVG(price) FROM Items
                    INNER JOIN Departments ON Departments.id = Items.department_id
                    INNER JOIN Shops ON Shops.id = Departments.shop_id
                    GROUP BY (Shops.name);
                        """)
            data = self.cur.fetchall()
            return data
        elif choice == 14:
            self.cur.execute("""
                            SELECT Shops.name, Items.name FROM Items
                            INNER JOIN Departments ON Departments.id = Items.department_id
                            INNER JOIN Shops ON Shops.id = Departments.shop_id;
                        """)
            data = self.cur.fetchall()
            new_data = {}
            for el in data:
                new_data.setdefault(el[0], []).append(el[1])
            return new_data


    # UPDATE METHOD

    def update_data(self):
        self.cur.execute("""
            UPDATE Items SET price = price + 100 WHERE name ~ '(^(B|b))|((E|e)$)'; 
        """)
        self.cur.commit()


    # DELETE METHODS

    def delete_data(self):
        self.cur.execute("""
                    DELETE FROM Items
                    WHERE price > 500 AND description IS NULL;
                """)
        self.cur.commit()

        self.cur.execute("""
            DELETE FROM Items WHERE id IN 
            (
                SELECT Items.id FROM Items
                INNER JOIN Departments ON Departments.id = Items.department_id
                INNER JOIN Shops ON Shops.id = department_id
                WHERE Shops.address is NULL
            )
        """)
        self.cur.commit()

        self.cur.execute("""
            DELETE FROM Items
            WHERE Items.id IN (
                SELECT id FROM Departments
                WHERE staff_amount < 225 
                OR staff_amount > 275
            );
        """)
        self.cur.commit()

        self.cur.execute("""
            TRUNCATE TABLE Shops CASCADE;
            TRUNCATE TABLE Departments CASCADE;
            TRUNCATE TABLE Items CASCADE;
        """)
        self.cur.commit()

    # DROP METHOD

    def drop_table(self):
        self.cur.execute("""DROP TABLE IF EXISTS Shops CASCADE ;""")
        self.cur.execute("""DROP TABLE IF EXISTS Departments CASCADE;""")
        self.cur.execute("""DROP TABLE IF EXISTS Items CASCADE;""")
        self.cur.commit()

