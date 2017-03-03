#!/usr/bin/python3
'''
lists all cities from the database hbtn_0e_4_usa
take 3 arguments: mysql username, mysql password and database name
'''
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], port=3306, db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    INNER JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC;")
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
