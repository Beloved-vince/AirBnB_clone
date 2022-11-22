#!/usr/bin/python3
<<<<<<< HEAD
"""This module contains the BaseModel class"""
import uuid
from datetime import datetime
import models
class BaseModel:
    """This class defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Instantiation of base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
    def __str__(self):
        """String representation of BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "Holberton"
    my_model.my_number = 89
    print(my_model)
    print(my_model.__dict__)
    print(my_model.to_dict())
    print(type(my_model.created_at))
    print(type(my_model.updated_at))
    print(type(my_model.to_dict()["created_at"]))
    print(type(my_model.to_dict()["updated_at"]))
    print(my_model.id)
    print(my_model.created_at) 
    print(my_model.updated_at)
    my_model.save()
    
=======
from uuid import uuid4
from datetime import datetime

class BaseModel():
    id = uuid4()

    def __init__(self, int=None):
        self.my_number = int
        self.name = str
        self.updated_at = datetime.now()
        self.id = self.id
        self.created_at = datetime.now()

    def __str__(self):
        """
        Return the following objects
        Args:
            class name:
                in format [BaseModel]
            id:
                to hold the unique class identifier
            created_at:
                        date object is created
            updated_at:
                        date object is updated
        """

        return ('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        save update_at anytime this function is call
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary containing key and value of the instance\
                including class name
        """

        dic = {}
        for key, value in self.__dict__.items():
            dic[key] = value
            if key in ["created_at", "updated_at"]:
                dic['created_at'] = self.created_at.isoformat()
                dic['updated_at'] = self.updated_at.isoformat()
                
        dic['__class__'] = self.__class__.__name__

        return dic
>>>>>>> a6d5d8a45b68386b917671b836ac99feb522a187
