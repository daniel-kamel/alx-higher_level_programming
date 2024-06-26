#!/usr/bin/python3
'''
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
'''

from sys import argv
import MySQLdb


def main():
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("""
                   SELECT * FROM states
                   WHERE name LIKE BINARY %s
                   ORDER BY id
                   """, (argv[4],))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
