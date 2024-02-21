#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(
        String(128), nullable=False
    )
    state_id = Column(
        String(60), ForeignKey('states.id'), nullable=False
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship(
            "Place",
            cascade="all, delete",
            backref="cities"
        )
    else:
        @property
        def places(self):
            """getter attr that returns the list of places instances"""
            from models import storage
            place_list = []
            places = storage.all(Place)
            for place in places.values():
                if place.city_id == self.id:
                    place_list.append(place)
            return place_list
