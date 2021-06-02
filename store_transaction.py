import sqlite3

#define connection and cursor

connection = sqlite3.connect ("store transactions.db")

cursor = connection.cursor()

# create stores table

command1 = """CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)"""

cursor.execute(command1)

# create purchase table

command2 = """CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT,
FOREIGN KEY(store_id) REFERENCES stores(store_id))"""

cursor.execute(command2)

# add to stores

cursor.execute ("INSERT INTO stores VALUES ( 21, 'Washington, DC')")
cursor.execute ("INSERT INTO stores VALUES ( 22, 'Rockville, MD')")
cursor.execute ("INSERT INTO stores VALUES ( 23, 'Bowie, MD')")

# add to purchases

cursor.execute ("INSERT INTO purchases VALUES (54, 21,  15.49)")
cursor.execute ("INSERT INTO purchases VALUES (77, 43, 21.12)")

# get results

cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()
print (results)


