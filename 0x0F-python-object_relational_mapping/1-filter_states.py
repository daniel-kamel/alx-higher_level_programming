#!/usr/bin/python3
'''
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
'''

from sys import argv
import MySQLdb


def main():
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("""
                   SELECT * FROM states
                   WHERE name LIKE BINARY 'N%' ORDER BY id
                   """)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
