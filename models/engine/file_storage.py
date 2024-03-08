#!/usr/bin/python3
"""Module for handling file storage"""

from models.base_model import BaseModel
import json


class FileStorage:
    """
    Class for serializing instances to a JSON file
    and deserializing JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in '__objects' the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file (path: '__file_path')"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to '__objects'"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for key, obj_data in obj_dict.items():
                class_name, obj_id = key.split('.')
                cls = None
                bases = (BaseModel,)
                namespace = obj_data
                cls = type(class_name, bases, namespace)
                self.__objects[key] = cls(**obj_data)
        except FileNotFoundError:
            pass
