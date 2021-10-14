import psycopg2
from psycopg2 import Error


class SQLManager:
    def __init__(self, dbname, db_user, password, hostname):
        self.dbname = dbname
        self.user = db_user
        self.password = password
        self.host = hostname
        self.conn = None
        self.cur = None

    # PRIVATE FUNC

    def __set_conn(self):
        try:
            self.conn = psycopg2.connect(user=self.user,
                                         password=self.password,
                                         host=self.host, database=self.dbname)
            print(f"Successfully connect to {self.dbname}")
        except (Exception, Error) as error:
            print("Error with work with PostgreSQL", error)

    def __set_cur(self):
        try:
            self.cur = self.conn.cursor()
            print(f"Successfully set cursor")
        except (Exception, Error) as error:
            print("Error with work with PostgreSQL", error)

    def __close_cur(self):
        try:
            self.cur.close()
        except (Exception, Error) as error:
            print("Error with work with PostgreSQL", error)

    def __close_conn(self):
        try:
            self.conn.close()
        except (Exception, Error) as error:
            print("Error with work with PostgreSQL", error)

    def __commit(self):
        try:
            self.conn.commit()
        except (Exception, Error) as error:
            print("Error with work with PostgreSQL", error)

    # USER METHODS

    def connect_to_db(self):
        self.__set_conn()
        self.__set_cur()
        print("You successfully connect to DB")

    def disconnect_from_db(self):
        self.__close_cur()
        self.__close_conn()
        print("You successfully disconnect from DB")

    # CREATE METHOD

    def create_table(self):
        try:
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
            self.__commit()
            print("You are successfully create tables")
        except (Exception, Error) as error:
            print("Error with work with PostgreSQL", error)

    # INSERT METHOD

    def insert_data(self):
        self.cur.execute("""
            INSERT INTO Shops(name, address, staff_amount) 
            VALUES (%s,%s,%s);
            """, ('Auchan', None, 250))
        self.__commit()
        self.cur.execute("""
            INSERT INTO Shops(name, address, staff_amount) 
            VALUES (%s,%s,%s);
            """, ('IKEA', 'Street Žirnių g. 56, Vilnius, Lithuania.', 500))
        self.__commit()

        self.cur.execute("""
                INSERT INTO Departments(sphere, staff_amount, shop_id) 
                VALUES (%s,%s,%s);
            """, ('Furniture', 250, 1))
        self.__commit()
        self.cur.execute("""
                INSERT INTO Departments(sphere, staff_amount, shop_id) 
                VALUES (%s,%s,%s);
            """, ('Furniture', 300, 2))
        self.__commit()
        self.cur.execute("""
                INSERT INTO Departments(sphere, staff_amount, shop_id) 
                VALUES (%s,%s,%s);
            """, ('Dishes', 200, 2))
        self.__commit()

        self.cur.execute("""
                INSERT INTO Items(name, description, price, department_id) 
                VALUES (%s,%s,%s,%s);
            """, ('Table', 'Cheap wooden table', 300, 1))
        self.__commit()

        self.cur.execute("""
                INSERT INTO Items(name, description, price, department_id) 
                VALUES (%s,%s,%s,%s);
            """, ('Table', None, 750, 2))
        self.__commit()

        self.cur.execute("""
                INSERT INTO Items(name, description, price, department_id) 
                VALUES (%s,%s,%s,%s);
            """, ('Bed', 'Amazing wooden bed', 1200, 2))
        self.__commit()

        self.cur.execute("""
                INSERT INTO Items(name, description, price, department_id) 
                VALUES (%s,%s,%s,%s);
            """, ('Cup', None, 10, 3))
        self.__commit()

        self.cur.execute("""
                INSERT INTO Items(name, description, price, department_id) 
                VALUES (%s,%s,%s,%s);
            """, ('Plate', 'Glass plate', 20, 3))
        self.__commit()
        print(
            "You are successfully insert data into Shops, Departments, Items")


    def select_1(self):
        self.cur.execute("""
            SELECT * FROM Items
            WHERE description IS NOT NULL;
        """)
        data = self.cur.fetchall()
        print(data)
        return data

    def select_2(self):
        self.cur.execute("""
                    SELECT DISTINCT sphere FROM Departments
                    WHERE staff_amount > 200;
                """)
        data = self.cur.fetchall()
        print(data)
        return data

    def select_3(self):
        self.cur.execute("""
                    SELECT address FROM Shops
                    WHERE name ~ '^(I|i)';
                """)
        data = self.cur.fetchall()
        print(data)
        return data

    def select_4(self):
        self.cur.execute("""
                    SELECT Items.name FROM Items
                    INNER JOIN Departments ON Departments.id = Items.department_id
                    WHERE Departments.sphere = 'Furniture';
                """)
        data = self.cur.fetchall()
        print(data)
        return data

    def select_5(self):
        self.cur.execute("""
                    SELECT Shops.name FROM Shops
                    INNER JOIN Departments ON Departments.shop_id = Shops.id
                    INNER JOIN Items ON Items.department_id = Departments.id
                    WHERE Items.description IS NOT NULL;
                """)
        data = self.cur.fetchall()
        print(data)
        return data

    def select_6(self):
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
        print(data)
        return data

    def select_7(self):
        self.cur.execute("""
                    SELECT id FROM Items
                    ORDER BY name
                    LIMIT 2
                    OFFSET 3;
                """)
        data = self.cur.fetchall()
        print(data)
        return data

    def select_8(self):
        self.cur.execute("""
                            SELECT Items.name, Shops.name FROM Items
                            INNER JOIN Departments ON Items.department_id = Departments.id
                            INNER JOIN Shops ON Shops.id = Departments.shop_id;
                        """)
        data = self.cur.fetchall()
        print(data)
        return data

    def select_9(self):
        self.cur.execute("""
                            SELECT Items.name, Departments.id FROM Items
                            LEFT JOIN Departments ON Items.department_id = Departments.id
                    """)
        data = self.cur.fetchall()
        print(data)
        return data

    def select_10(self):
        self.cur.execute("""
                            SELECT Items.name, Departments.id FROM Items
                            RIGHT JOIN Departments ON Items.department_id = Departments.id
                        """)
        data = self.cur.fetchall()
        print(data)
        return data

    def select_11(self):
        self.cur.execute("""
                            SELECT Items.name, Departments.id FROM Items
                            FULL JOIN Departments ON Items.department_id = Departments.id
                    """)
        data = self.cur.fetchall()
        print(data)
        return data

    def select_12(self):
        self.cur.execute("""
                            SELECT Items.name, Shops.name FROM Items
                            CROSS JOIN Departments
                            INNER JOIN Shops ON Shops.id = Departments.shop_id;
                    """)
        data = self.cur.fetchall()
        print(data)
        return data

    def select_13(self):
        self.cur.execute("""
                SELECT Shops.name, COUNT(*) as count_goods, SUM(price),
                MAX(price), MIN(price),
                AVG(price) FROM Items
                INNER JOIN Departments ON Departments.id = Items.department_id
                INNER JOIN Shops ON Shops.id = Departments.shop_id
                GROUP BY (Shops.name);
                    """)
        data = self.cur.fetchall()
        print(data)
        return data

    def select_14(self):
        self.cur.execute("""
                        SELECT Shops.name, Items.name FROM Items
                        INNER JOIN Departments ON Departments.id = Items.department_id
                        INNER JOIN Shops ON Shops.id = Departments.shop_id;
                    """)
        data = self.cur.fetchall()
        new_data = {}
        for el in data:
            new_data.setdefault(el[0], []).append(el[1])
        print(new_data)
        return new_data

    # UPDATE METHOD

    def update_data(self):
        try:
            self.cur.execute("""
                UPDATE Items SET price = price + 100 WHERE name ~ '(^(B|b))|((E|e)$)'; 
            """)
            self.__commit()
        except (Exception, Error) as error:
            print("Error with work with PostgreSQL", error)

    # DELETE METHODS

    def delete_1(self):
        self.cur.execute("""
            DELETE FROM Items
            WHERE price > 500 AND description IS NULL;
        """)
        self.__commit()
        print("You are successfully delete data from tables")

    def delete_2(self):
        self.cur.execute("""
            DELETE FROM Items WHERE id IN 
            (
                SELECT Items.id FROM Items
                INNER JOIN Departments ON Departments.id = Items.department_id
                INNER JOIN Shops ON Shops.id = department_id
                WHERE Shops.address is NULL
            )
        """)
        self.__commit()
        print("You are successfully delete data from tables")

    def delete_3(self):
        self.cur.execute("""
            DELETE FROM Items
            WHERE Items.id IN (
                SELECT id FROM Departments
                WHERE staff_amount < 225 
                OR staff_amount > 275
            );
        """)
        self.__commit()
        print("You are successfully delete data from tables")

    def delete_4(self):
        self.cur.execute("""
            TRUNCATE TABLE Shops CASCADE;
            TRUNCATE TABLE Departments CASCADE;
            TRUNCATE TABLE Items CASCADE;
        """)
        self.__commit()
        print("You are successfully delete data from tables")

    # DROP METHOD

    def drop_table(self):
        try:
            self.cur.execute("""DROP TABLE IF EXISTS Shops CASCADE ;""")
            self.cur.execute("""DROP TABLE IF EXISTS Departments CASCADE;""")
            self.cur.execute("""DROP TABLE IF EXISTS Items CASCADE;""")
            self.__commit()
            print("You are successfully drop tables")
        except (Exception, Error) as error:
            print("Error with work with PostgreSQL", error)
