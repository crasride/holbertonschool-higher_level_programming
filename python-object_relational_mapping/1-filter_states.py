#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
take 3 arguments
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id ASC")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
    c.close()
    db.close()
