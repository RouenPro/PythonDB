import psycopg2
from pprint import pprint


class DatabaseConnection:

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname = 'Pythondb' user='postgres' host='localhost' password = 'password' port='49388'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("Hello world")

        except:
            pprint("Cannot connected")

    # def create_table(self):
    #     create_table_command = "CREATE TABLE pet(id serial PRIMARY KEY, name varchar(100), age integer NOT NULL )"
    #     self.cursor.execute(create_table_command)


if __name__ == '__main__':
    database_connection = DatabaseConnection()



