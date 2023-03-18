#!/usr/bin/python3
"""script that prints the first State
    object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    stmt = "SELECT * FROM states WHERE id=1"
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            if row is not None:
                print(f"{row[0]}: {row[1]}")
