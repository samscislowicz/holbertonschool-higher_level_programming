#!/usr/bin/python3
'''
a script that lists all states from the database hbtn_0e_0_usa
takes 3 arguments: mysql username, mysql password and database name

'''
import MySQLdb
import sys

if __name__=="__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2],
                         port=3306, db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
