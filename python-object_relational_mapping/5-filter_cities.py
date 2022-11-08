#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
take 3 arguments
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states,cities \
              WHERE states.id=cities.state_id \
              ORDER BY cities.id ASC")
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
    c.close()
    db.close()
