#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from importlib import import_module


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """initialize filestorage instance"""
        self.model_classes ={
            'BaseModel': import_module('models.base_model').BaseModel,
            'User': import_module('models.user').User,
            'Place': import_module('models.place').Place,
            'City': import_module('models.city').City,
            'State': import_module('models.state').State,
            'Review': import_module('models.review').Review,
            'Amenity': import_module('models.amenity').Amenity
            }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        else:
            fd = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    fd[key] = value
            return fd

    def delete(self, obj=None):
        """Removes an object from the storage dictionary"""
        if obj is not None:
            obj_key = obj.dict()['__class__'] + '.' + obj.id
            if obj_key in self.__objects.keys():
                del self.__objects[obj_key]

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects.update({obj.to_dict()['__class__'] +
            '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            for key, val in self.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """reload file"""
        if os.path.isfile(self.__file_path):
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, value in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)

    def close(self):
        """closes storage engine"""
        self.reload()
