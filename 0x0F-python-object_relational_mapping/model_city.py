#!/usr/bin/python3
"""python file that contains the class definition of a
    City and an instance Base = declarative_base()"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    State class attribute that inherits from base
    """

    __tablename__ = "cities"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, nullable=False)
