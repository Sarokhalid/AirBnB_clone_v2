#!/usr/bin/python3
"""manage database storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import urllib.parse
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place, place_amenity
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """manage storage of hbnb models in a sql database"""
    __engine = None
    __session = None

    def __init__(self):
        """initialize SQL databsse storage"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', default='localhost')
        database = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return dictionary of models"""
        objects = {}
        classes = (User, State, City, Amenity, Place, Review)
        if cls is not None:
            query = self.session.query(cls).all()
            for obj in query:
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            for cls in classes:
                query = self.session.query(cls).all()
                for obj in query:
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    objects[key] = obj
            return objects

    def delete(self, obj=None):
        """Remove object from storage"""
        if obj is not None:
            self.__session.delete(obj)

    def new(self, obj):
        """add new object to storage database"""
        self.__session.add(obj)

    def save(self):
        """commits settions change database"""
        self.__session.commit()

    def reload(self):
        """loads storage database"""
        Base.metadata.create_all(self.__engine)
        SessionFactory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        Settion = scoped_session(SessionFactory)
        self.__session = Session()

    def close(self):
        """close storge database"""
        self.__session.close()
