

import csv, sqlite3

con = sqlite3.connect("t1.db")
cur = con.cursor()
cur.execute("CREATE TABLE t (col1, col2);")

with open('testing','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['col1'], i['col2']) for i in dr]

cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
con.commit()


