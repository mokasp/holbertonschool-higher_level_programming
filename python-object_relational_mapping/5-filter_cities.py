#!/usr/bin/python3
""" module that lists all cities that match user input from SQL database """
import MySQLdb
import sys


def main(un, pw, db_name, state_name):
    """ function that connects to SQL database and prints list \
        of cities from state that match user input"""
    text = "SELECT cities.name FROM cities INNER \
        JOIN states ON states.id = cities.state_id WHERE states.name = %s \
            ORDER BY cities.id"
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=f"{un}", passwd=f"{pw}",
                           db=f"{db_name}", charset="utf8")
    cur = conn.cursor()
    cur.execute(text, (state_name,))
    query_rows = cur.fetchall()
    i = 0
    for row in query_rows:
        i += 1
        for col in row:
            if i < len(query_rows):
                print(f"{col}, ", end="")
            else:
                print(col)
    cur.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        pass
