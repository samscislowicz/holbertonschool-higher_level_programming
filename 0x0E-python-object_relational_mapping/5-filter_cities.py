#!/usr/bin/python3
'''
takes in the name of a state as an argument and lists all cities of that state
take 3 arguments: mysql username, mysql password and database name
'''
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], port=3306, db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    INNER JOIN states ON states.id = cities.state_id AND states.name = %s\
    ORDER BY cities.id ASC;", (sys.argv[4],))

    listoutput = []
    for row in cur.fetchall():
        listoutput.append(row[1])
    print(', '.join(listoutput))

    cur.close()
    db.close()
