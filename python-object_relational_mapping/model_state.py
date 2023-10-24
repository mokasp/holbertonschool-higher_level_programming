#!/usr/bin/python3
""" module containing python class State to map to SQL table"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    create_engine,
    inspect,
    Column,
    String,
    Integer)

Base = declarative_base()


class State(Base):
    """ class to represent a state, to map to SQL table """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
