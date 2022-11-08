#!/usr/bin/python3
"""
takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argumenttake 4 arguments
But this time, write one that is safe from MySQL injections!
take 4 arguments
fetchall() method, which fetches all rows from the last executed statement
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id ASC")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
    c.close()
    db.close()
