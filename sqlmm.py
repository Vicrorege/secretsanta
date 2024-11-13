import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
first_name VARCHAR,
last_name VARCHAR,
username VARCHAR,
real_name VARCHAR,
real_surname VARCHAR,
role INTEGER,
typemsg VARCHAR,
FOREIGN KEY (role)  REFERENCES roles(id))""")


# cur.execute("""CREATE TABLE IF NOT EXISTS roles(
# id INTEGER PRIMARY KEY,
# name VARCHAR)""")


cur.close()
conn.close()