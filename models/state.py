#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            "City",
            cascade="all, delete",
            backref="state"
        )
    else:
        @property
        def cities(self):
            """return cities in state"""
            from models import storage
            city_list = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
