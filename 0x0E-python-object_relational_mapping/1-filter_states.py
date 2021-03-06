#!/usr/bin/python3
'''
lists all states with a name starting with N from the database hbtn_0e_0_usa
take 3 arguments: mysql username, mysql password and database name
'''
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], port=3306, db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    for row in cur.fetchall():
        if row[1][0] == "N":
            print(row)

    cur.close()
    db.close()
