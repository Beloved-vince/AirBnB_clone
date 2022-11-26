#!/usr/bin/python3
"""
BaseModel class is created to generate a dictionary representation\
        of an instance
On this class other classes will inherit from
"""
import models
from uuid import uuid4
from datetime import datetime
format_dt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """
    Methos:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """Args:
                *args: Constructor of BaseModel set to "None"
                **kwargs: Constructor of BaseModel
        if **kwargs is not empty operation can be perform
        """
        if kwargs:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return the following objects
            class name: in format [BaseModel]
            id: to hold the unique class identifier
            created_at: date object is created
            updated_at: date object is updated
        """
        class_name = self.__class__.__name__
        uuid = self.id
        class_dict = self.__dict__
        return '[{}] ({}) {}'.format(class_name, uuid, class_dict)

    def save(self):
        """
        save update_at anytime this function is call
        """
        self.updated_at = datetime.now()
        models.storage.save()

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
    
    
    @classmethod
    def all(cls):
        """Retrieve all current instances of cls"""
        return models.storage.find_all(cls.__name__)

    @classmethod
    def count(cls):
        """Get the number of all current instances of cls"""
        return len(models.storage.find_all(cls.__name__))

    @classmethod
    def create(cls, *args, **kwargs):
        """Creates an Instance"""
        new = cls(*args, **kwargs)
        return new.id

    @classmethod
    def show(cls, instance_id):
        """Retrieve an instance"""
        return models.storage.find_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def destroy(cls, instance_id):
        """Deletes an instance"""
        return models.storage.delete_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def update(cls, instance_id, *args):
        """Updates an instance
        if args has one elem and its a dict:
        it updates by key value
        else:
        updates by first being key and second being value"""
        if not len(args):
            print("** attribute name missing **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_one(
                cls.__name__,
                instance_id,
                *arg
            )
