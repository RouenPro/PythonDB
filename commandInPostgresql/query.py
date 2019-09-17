import psycopg2

# connect to Database postgres
con = psycopg2.connect(
    host = "localhost",
    database = "Pythondb2",
    user = "postgres",
    password = "password")

cur = con.cursor()
cur.execute("
SELECT id, POW(f1 - :e1, 2) + POW(f2 - :e2, 2) + ... + POW(f128 - :e128, 2) AS square_distance
FROM encodings
WHERE
 f1 > :minF1 AND f1 < :maxF1 AND
 f2 > :minF2 AND f2 < :maxF2 AND
 f128 > :minF128 AND f128 < :maxF128
ORDER BY square_distance ASC LIMIT 1",(200, "RouenPro"))
print("Finish")
