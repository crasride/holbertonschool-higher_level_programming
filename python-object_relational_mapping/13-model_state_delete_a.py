#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a the
database hbtn_0e_6_usa
You must use the module SQLAlchemy
take 3 arguments
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
    # changes the name of State Arizona
    for state in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(state)
    session.commit()
    session.close()
