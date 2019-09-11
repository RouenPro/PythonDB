import psycopg2

class ConnectDB:
    try:
        con = psycopg2.connect(database="Pythondb2", user="postgres", password="password", host="127.0.0.1", port="52848")
        print("Database opened successfully")
    except Exception as e:
        print("Database not connected")
