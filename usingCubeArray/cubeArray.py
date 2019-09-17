import psycopg2

conn = psycopg2.connect(host = "localhost",
database = "Pythondb",
user = "postgres",
password = "password")

cur = conn.cursor()

tempstring = """SELECT first_name FROM wanted ORDER BY face_encoding <-> cube(array["+face_encoding_string+"]) LIMIT 1"""

cur.execute(tempstring)

print(cur.fetchall())
print("---------Completed----------")
