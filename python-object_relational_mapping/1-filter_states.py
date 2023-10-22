#!/usr/bin/python3
""" script that lists all rows that start with N from SQL database """
import MySQLdb
import sys


def main():
    """ function that connects to SQL database and prints list \
        of states that start with N"""
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=f"{sys.argv[1]}", passwd=f"{sys.argv[2]}",
                           db=f"{sys.argv[3]}", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' \
                ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
