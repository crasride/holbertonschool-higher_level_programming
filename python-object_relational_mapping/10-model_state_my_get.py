#!/usr/bin/python3
"""
prints the State object with name passed as argument the database hbtn_0e_6_usa
You must use the module SQLAlchemy
take 4 arguments
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # MySQL connection using mysqldb driver
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break
    if found is False:
        print("Not found")
    session.close()
