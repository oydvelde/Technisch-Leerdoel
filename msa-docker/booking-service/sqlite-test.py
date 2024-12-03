import sqlite3

db_path = './data/booking-database.db'
createfile = './setup/createfile.sql'

with open(createfile, 'r') as file:
    sql_script = file.read()

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

cursor.executescript(sql_script)

connection.commit()
connection.close()