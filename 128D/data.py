import psycopg2
import numpy as np
from psycopg2.extras import execute_values
import psycopg2
import argparse
import sys
import re
import numpy as np
import os
import psycopg2.extras


x = np.array([-0.12317917  ,0.1295325   ,0.02713361 ,-0.06005447 ,-0.02224888 ,-0.02827183
 ,-0.02702068 ,-0.13983949  ,0.15303117 ,-0.15798856  ,0.29225576 ,-0.04453279
 ,-0.2672587  ,-0.11455585 ,-0.03339733  ,0.16091156 ,-0.23091689 ,-0.13674957
 ,-0.02400368  ,0.03506713  ,0.09696344 ,-0.06715634  ,0.066604    ,0.03599105
 ,-0.13838136 ,-0.36371985 ,-0.15504265 ,-0.08416935 ,-0.00856027 ,-0.05043825
 ,-0.05030803 ,-0.03930286 ,-0.27487001 ,-0.06733396 ,-0.0638352   ,0.0151922
 ,-0.03263801 ,-0.01752208  ,0.17831501  ,0.03792501 ,-0.15837005 ,-0.02159197
 ,-0.00805986  ,0.27534035  ,0.15590662  ,0.09286211  ,0.01821787 ,-0.13260651
  ,0.1091216  ,-0.21156202  ,0.05751346  ,0.13857645  ,0.03397972  ,0.05412437
 ,-0.02756266 ,-0.12669945  ,0.06082204  ,0.11565815 ,-0.1724897   ,0.06117474
  ,0.10689712 ,-0.06610599 ,-0.045127   ,-0.02818304  ,0.28090265  ,0.07655993
 ,-0.13833436 ,-0.13245125  ,0.14463113 ,-0.08954298  ,0.02075369  ,0.03335764
 ,-0.16492787 ,-0.23127696 ,-0.307549    ,0.07759047  ,0.3731384   ,0.0849002
 ,-0.11596628  ,0.03577663 ,-0.09306946  ,0.00843453  ,0.14352767  ,0.1284668
 ,-0.02896055  ,0.03218747 ,-0.1388545   ,0.08272229  ,0.17906588 ,-0.08510893
 ,-0.01768984  ,0.25436538 ,-0.05504991  ,0.0683517   ,0.04100956  ,0.05838982
 ,-0.11346739  ,0.05069625 ,-0.14242364  ,0.06367792  ,0.05416217 ,-0.04006049
 ,-0.04667467  ,0.08582801 ,-0.07238141  ,0.07154582 ,-0.00425951  ,0.00640353
 ,-0.01968569 ,-0.08184984 ,-0.15997154 ,-0.12082902  ,0.06816939 ,-0.22806759
  ,0.21343666  ,0.17385238  ,0.02772689  ,0.11796317  ,0.11827657  ,0.08486905
 ,-0.02354596  ,0.00751721 ,-0.23072748  ,0.00631592  ,0.13620441 ,-0.00589077
  ,0.09612961 ,-0.05096926],dtype=np.float)

x = np.array2string(x, precision=3)
print(x)
print(type(x))
print(len(x))

con = psycopg2.connect(
    host = "localhost",
    database = "Pythondb",
    user = "postgres",
    password = "password")

print("---------Hello-----------")
a = np.linspace(start = -5, stop = 150,
                num = 128, endpoint = True)

print("Graphical Representation : \n", np.cbrt(a))
print(type(np.cbrt(a)))
print("---------Thank you------------")

east = np.linspace(-180.0,180.0,num=50)
north = np.linspace(-90.0,90.0,num=50)
# get array of pairs [east, north]
coor = np.dstack([east, north])

# convert to array of tuples (east, north) as strings
values = [[str(tuple(i))] for i in coor[0]]
#cursor
cur = con.cursor()
# Random value

#
values = map(lambda a: ['{},{}'.format(a[0],a[1])], np.column_stack((east, north)))
print(type(values))
print("Hello world**")
# psycopg2.extras.execute_values(cur, "insert into employees (id, username) values (%s, %s)", (1111, "R"))
psycopg2.extras.execute_values(cur, "INSERT INTO employees (id, username) VALUES (%s, %s)", (1,values))

# cur.execute("insert into employees (id, username) values (%s, %s)",(1111, "R"))

#execute query bnm,7890 qwertyop
cur.execute("select id, username from employees")

# Query Result Set
rows = cur.fetchall()

# for r in rows:
#     print (f"id {r[0]} username {r[1]}")

#commit the transcation
con.commit()

#close the cursor
cur.close()

#close the connection
con.close()
