#!/usr/bin/python3
""" module that connects to SQL server and updates name of entry to table
States"""
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
    the_state = session.query(State)
    the_state = the_state.filter(State.id == 2)
    thing = the_state.one()
    thing.name = 'New Mexico'
    session.commit()
    session.close()
