#!/usr/bin/python3
"""script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    text = "SELECT * FROM states WHERE name LIKE '{}' \
            ORDER BY id ASC".format(sys.argv[4])
    cur.execute(text)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
