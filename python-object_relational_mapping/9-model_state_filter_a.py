#!/usr/bin/python3
"""
lists all State objects that contain letter from the database hbtn_0e_6_usa
You must use the module SQLAlchemy
take 3 arguments
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # MySQL connection using mysqldb driver
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    s = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for state in s:
        print("{}: {}".format(state.id, state.name))
    session.close()
