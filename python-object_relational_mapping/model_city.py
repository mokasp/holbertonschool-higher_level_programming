#!/usr/bin/python3
""" module containing python class City to map to SQL table"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey)

Base = declarative_base()


class City(Base):
    """ class to represent a city, to map to SQL table """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
