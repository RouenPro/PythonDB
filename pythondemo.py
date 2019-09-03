import psycopg2

# Connect to database
con = psycopg2.connect(
    host = "localhost",
    database = "Pythondb",
    user = "postgres",
    password = "password")

import psycopg2

#cursor
cur = con.cursor()

cur.execute("insert into employees (id, username) values (%s, %s)", (1, "Hussein") )

#execute query
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
