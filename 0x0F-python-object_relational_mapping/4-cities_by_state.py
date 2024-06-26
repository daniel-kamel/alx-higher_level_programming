#!/usr/bin/python3
'''
Script that lists all cities from the database hbtn_0e_4_usa
'''

from sys import argv
import MySQLdb


def main():
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("""
                   SELECT cities.id, cities.name, states.name
                   FROM cities
                   JOIN states
                   ON cities.state_id = states.id
                   ORDER BY cities.id
                   """)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
