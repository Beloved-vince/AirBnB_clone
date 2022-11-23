#!/usr/bin/python3
"""
This module contains where object serialization and \
will take place \

All object will be passed to json format in a dictionary \
        format
"""
from models.base_model import BaseModel
from json import dump, dumps, load


class FileStorage(BaseModel):
    """
    Args:
        FileStorage:
                    The filestorage store object in json format
        __file_path: Path to json file
        __objects: Private attribute to store all object by <class name>.id
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Return private attribute __objects in dictionary format
        """
        return self.__objects

    def new(self, obj):
        """
        Args:
            obj: sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__+'.'+obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializing __object into JSON file (path: __file_path)
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', 'utf-8') as file:
            dump(new_dict, file)
