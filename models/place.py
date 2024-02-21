#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from models.review import Review


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        nullable=False,
        primary_key=True
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        nullable=False,
        primary_key=True
    )
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(
        String(60), ForeignKey('cities.id'), nullable=False
    )
    user_id = Column(
        String(60), ForeignKey('users.id'), nullable=False
    )
    name = Column(
        String(128), nullable=False
    )
    description = Column(
        String(1024), nullable=True
    )
    number_rooms = Column(
        Integer, nullable=False, default=0
    )
    number_bathrooms = Column(
        Integer, nullable=False, default=0
    )
    max_guest = Column(
        Integer, nullable=False, default=0
    )
    price_by_night = Column(
        Integer, nullable=False, default=0
    )
    latitude = Column(
        Float, nullable=True
    )
    longitude = Column(
        Float, nullable=True
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relasionship(
            "Review",
            cascade="all, delete",
            backref="place"
        )
        amenities = relatioship(
            "Amenity",
            secondary=place_amenity,
            Viewonly=False
        )
    else:
        @property
        def reviews(self):
            """getter attr that return list of review instace"""
            from models import storage
            review_list = []
            reviews = storage.all(Review)
            for review in reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
        @property
        def amenities(self):
            """getter attribute return list of amenity instances"""
            from models import storage
            amenity_list = []
            amenities = storage.all(Amenity)
            for amenity in amenities.values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
                return amenity_list

        @amenities.setter
        def amenities(self, amenity):
            """setter attributes"""
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
