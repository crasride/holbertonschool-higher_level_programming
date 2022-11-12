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
from model_state import State
from model_city import City

if __name__ == "__main__":
    # MySQL connection using mysqldb driver
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    s = Session()
    # changes the name of State Arizona
    for city, state in s.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    s.close()
