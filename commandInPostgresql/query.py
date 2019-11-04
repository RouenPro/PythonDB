import psycopg2

# connect to Database postgres
con = psycopg2.connect(
    host = "localhost",
    database = "Pythondb2",
    user = "postgres",
    password = "password")

cur = con.cursor("""SELECT * from my_stored_encodings ORDER BY sqrt(
power(-0.12317917 - -0.12317917, 2) +
power(0.1295325 - 0.1295325, 2))""")
cur.execute("")
print("Finish")
