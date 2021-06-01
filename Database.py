import sqlite3

db = sqlite3.connect('Registration')
rs = db.cursor()
rs.execute('create table Register(name varchar(50))')
