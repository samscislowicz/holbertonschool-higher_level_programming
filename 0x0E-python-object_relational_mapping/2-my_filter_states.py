#!/usr/bin/env python3
'''
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
'''


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], port=3306, db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name\
    LIKE '{}' ORDER BY id ASC;".format(sys.argv[4]))
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
