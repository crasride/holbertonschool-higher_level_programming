#!/usr/bin/python3
"""
that lists all State objects from the database hbtn_0e_6_usa
You must use the module SQLAlchemy
take 3 arguments
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # session is an instance of the (sessionmaker) class unique
    Session = sessionmaker(bind=engine)
    for state in Session().query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    Session().close()
"""
Boolean, if True will enable the connection pool "pre-ping" feature that
tests connections max 3 times.
"""
