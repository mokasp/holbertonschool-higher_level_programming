#!/usr/bin/python3
""" script that lists all cities and states from joined tables in SQL
database """
import MySQLdb
import sys


def main(un, pw, db_name):
    """ function that connects to SQL database and prints list \
        of cities and their corresponding states"""
    text = "SELECT cities.id, cities.name, states.name FROM cities INNER \
        JOIN states ON states.id = cities.state_id ORDER BY cities.id"
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
    main(sys.argv[1], sys.argv[2], sys.argv[3])
