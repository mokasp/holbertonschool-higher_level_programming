#!/usr/bin/python3
""" script that lists all rows that match user input from SQL database """
import MySQLdb
import sys


def main(un, pw, db_name, state_name):
    """ function that connects to SQL database and prints list \
        of states that match user input"""
    text = "SELECT id, name FROM states WHERE name = '{:s}' \
                ORDER BY id ASC".format(state_name)
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=f"{un}", passwd=f"{pw}",
                           db=f"{db_name}", charset="utf8")
    cur = conn.cursor()
    cur.execute(text)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
