#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from importlib import import_module


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def reload(self):
        """initialize filestorage instance"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.state import State
        from models.review import Review
        from amenity import Amenity
        classes = {
            'BaseModel': import_module('models.base_model').BaseModel,
            'User': import_module('models.user').User,
            'State': import_module('models.state').State,
            'City': import_module('models.city').City,
            'Amenity': import_module('models.amenity').Amenity,
            'Place': import_module('models.place').Place,
            'Review': import_module('models.review').Review
        }
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls_name = val['__class__']
                    if cls_name in classes:
                        self.all()[key] = classes[cls_name](**val)
        except FileNotFoundError:
            pass

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            objects_of_cls = {}
            for key, obj in FileStorage.__objects.items():
                if cls.__name__ == obj.__class__.__name__:
                    objects_of_cls[key] = obj
            return objects_of_cls

    def delete(self, obj=None):
        """Removes an object from the storage dictionary"""
        if obj is None:
            return
        key = obj.__class__.__name__ + '.' + obj.id
        if key in self.all():
            del self.all()[key]

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all()[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            for key, val in FileStorage__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def close(self):
        """closes storage engine"""
        self.reload()
