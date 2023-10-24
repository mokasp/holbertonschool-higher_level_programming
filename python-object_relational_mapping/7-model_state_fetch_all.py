#!/usr/bin/python3
""" module that connects to SQL server and lists all states in table States"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import (sessionmaker)


if __name__ == "__main__":
    un = sys.argv[1]
    pw = sys.argv[2]
    dbn = sys.argv[3]
    text = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(text.format(un, pw, dbn), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
