#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(
        String(128), nullable=False
    )
    password = Column(
        String(128), nullable=False
    )
    first_name = Column(
        String(128), nullable=True
    )
    last_name = Column(
        String(128), nullable=True
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship(
            "Place",
            cascade="all, delete",
            backref="user"
        )
        reviews = relationship(
            "Review",
            cascade="all, delete",
            backref="user"
        )
    else:
        @property
        def places(self):
            """getter attribute retuen list of places instances"""
            from models import storage
            place_list = []
            places = storage.all(Place)
            for place in places.values():
                if place.user_id == self.id:
                    place_list.append(place)
            return place_list

        @property
        def reviews(self):
            """getter attribute retuen list of review instances"""
            from models import storage
            review_list = []
            reviews = storage.all(Review)
            for review in reviews.values():
                if review.user_id == self.id:
                    review_list.append(review)
            return review_list
