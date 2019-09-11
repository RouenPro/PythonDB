try:
conn = psycopg2.connect("host=localhost dbname=Pythondb user=postgres password=password " )
curr = conn.cursor()
curr.execute("""INSERT INTO CITY (name) values (%s);""",(cities))
conn.commit()
curr.close()
conn.close()
