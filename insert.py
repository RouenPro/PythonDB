import psycopg2
import numpy as np
from psycopg2.extras import execute_values


b = np.random.randn(128)
print("-----------------")
print(type(b))

# con = psycopg2.connect(
#     host = "localhost",
#     database = "Pythondb",
#     user = "postgres",
#     password = "password")

east = np.linspace(-180.0,180.0,num=100)
north = np.linspace(181.0,90.0,num=100)
coor = np.vstack([east, north])

conn = psycopg2.connect(host = "localhost",
database = "Pythondb",
user = "postgres",
password = "password")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS foobar;")
cur.execute("CREATE TABLE foobar (coordinate   point);")

# Working for an coordinate example:
cur.execute("INSERT INTO foobar VALUES (('12.56,56.43'));")

# Working for 1st coordinate in coor:
tmp = ','.join(str(e) for e in coor[:,0])
cur.execute('INSERT INTO foobar VALUES (point(' + tmp + '));')

# NOT WORKING!!!
# Insert all points in one go:
# cur.execute('INSERT INTO foobar VALUES (coor);')

conn.commit()

b = [['(-180.0, -90.0)'],
 ['(-140.0, -70.0)'],
 ['(-100.0, -50.0)'],
 ['(-60.0, -30.0)'],
 ['(-20.0, -10.0)'],
 ['(20.0, 10.0)'],
 ['(10.0, 30.0)'],
 ['(100.0, 50.0)'],
 ['(140.0, 70.0)'],
 ['(180.0, 90.0)'],
 ['(-180.0, -90.0)'],
 ['(-140.0, -70.0)'],
 ['(-100.0, -50.0)'],
 ['(-60.0, -30.0)'],
 ['(-20.0, -10.0)'],
 ['(20.0, 10.0)'],
 ['(10.0, 30.0)'],
 ['(100.0, 50.0)'],
 ['(140.0, 70.0)'],
 ['(181.0, 90.0)']

 ]

#cursor
east = np.linspace(-180.0, -90.0,num=128)
north = np.linspace(181.0, 90.0,num=128)


# get array of pairs [east, north]
coor = np.dstack([east, north])

# convert to array of tuples (east, north) as strings
values = [[str(tuple(i))] for i in coor[0]]

execute_values(cur, 'INSERT INTO foobar VALUES %s', values)

conn.commit()

print("--------Completed--------")
