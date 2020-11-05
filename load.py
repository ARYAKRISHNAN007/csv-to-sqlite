import sqlite3
import csv
import sys

conn=sqlite3.connect(sys.argv[1].split('.')[0] + '.sqlite3')
c=conn.cursor()

c.execute("""CREATE TABLE data(
								number,
								dt date,
								start time,
								visitor text,
								pts number,
								home text,
								pts1 number,
								unname6 text,
								unname7 text,
								attend number,
								notes text
			) """)

a_file = open(sys.argv[1],"r")
rows = csv.reader(a_file)

c.executemany("INSERT INTO data VALUES (?,?,?,?,?,?,?,?,?,?,?)", rows)

c.execute("SELECT rowid,* FROM data")
p=c.fetchall()
for i in p:
	print(i)

conn.commit()
conn.close()
