#!/usr/bin/python3
'''
lists all State objects from the database hbtn_0e_6_usa
Results must be sorted in ascending order by states.id
'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    sessionm = sessionmaker(bind=engine)
    session = sessionm()
    for instance in session.query(State).order_by(State.id):
        if 'a' in instance.name:
            print("{}: {}".format(instance.id, instance.name))
