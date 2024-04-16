#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_object = session.query(State).filter_by(id=2).first()
    new_object.name = 'New Mexico'
    session.commit()


if __name__ == "__main__":
    main()
