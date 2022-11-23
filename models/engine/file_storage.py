#!/usr/bin/python3
"""
This module contains where object serialization and \
will take place \

All object will be passed to json format in a dictionary \
        format
"""
from os.path import exists
from models.base_model import BaseModel
from json import dump, dumps, load


class FileStorage():
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
        class_name = obj.__class__.__name__
        class_id = obj.id
        key = class_name + "." + class_id
        self.__objects[key] = obj

    def save(self):
        """
        Serializing __object into JSON file (path: __file_path)
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            dump(new_dict, file)

    def reload(self):
        """
        Return the deserializes the JSON file to __objects \
                (only if the JSON file (__file_path) exists ; \
                otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        
        dic_obj = {}
        FileStorage.__objects = {}
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as fil:
                dic_obj = load(fil)
                for key, value in dic_obj.items():
                    class_nam = key.split(".")[0]
                    FileStorage.__objects[key] = eval(class_nam)(**value)
                    
                    if class_nam in name_class:
                        FileStorage.__objects[key] = eval(class_nam)(**value)
                    else:
                        pass
        else:
            pass
        