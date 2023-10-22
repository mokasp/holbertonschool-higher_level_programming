#!/usr/bin/python3
""" script that lists all rows from SQL database"""
import MySQLdb
import sys

def main():
    conn = MySQLdb.connect(host="localhost", port=3306, user=f"{sys.argv[1]}", passwd=f"{sys.argv[2]}", db=f"{sys.argv[3]}", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
