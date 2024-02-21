#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os


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
        from models.amenity import Amenity
        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name = val['__class__']
                    obj = classes[class_name](**val)
                    FileStorag.__objects[key] = obj
        except FileNotFoundError:
            pass

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return list(FileStorage.__objects.values())
        else:
            return [obj for obj in FileStorage.__objects.values()
                    if isinstance(obj, cls)]

    def delete(self, obj=None):
        """Removes an object from the storage dictionary"""
        if obj is not None and obj.id in self.__objects:
            del self.__objects[obj.id]

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().append(obj)

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        for key, val in FileStorage.__objects.items():
            temp[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(temp, f)

    def close(self):
        """closes storage engine"""
        self.reload()
