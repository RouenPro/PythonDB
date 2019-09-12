import psycopg2
import numpy as np
from psycopg2.extras import execute_values



b = np.random.randn(128)
print("-----------------")
print(type(b))
print("-----------------")
print(b)

print("------------------")
x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print(type(x))
print(x)
print("------------------")


# Connect to database
con = psycopg2.connect(
    host = "localhost",
    database = "Pythondb",
    user = "postgres",
    password = "password")

#cursor
cur = con.cursor()

cur.execute("insert into employees (id, username) values (%s, %s)",(200, "YesssssNo"))

#execute query bnm,7890 qwertyop
cur.execute("select id, username from employees")

rows = cur.fetchall()

for r in rows:
    print (f"id {r[0]} username {r[1]}")

#commit the transcation
con.commit()

#close the cursor
cur.close()

#close the connection
con.close()
