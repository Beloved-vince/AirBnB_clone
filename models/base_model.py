#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models
"""
BaseModel class is created to generate a dictionary representation\
        of an instance
On this class other classes will inherit from
"""

format_dt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():

    def __init__(self, *args, **kwargs):
        """Args:
                *args: Constructor of BaseModel set to "None"
                **kwargs: Constructor of BaseModel
        if **kwargs is not empty operation can be perform
        """
        if args:
            pass
        if kwargs is not None:
            for key, item in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.strptime(item, format_dt)
                if key not in ['__class__']:
                    setattr(self, key, item)
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

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
        class_name = self.__class__.__name__
        uuid = self.id
        class_dict = self.__dict__
        return '[{}] ({}) {}'.format(class_name, uuid, class_dict)

    def __repr__(self):
        """
        returns string representation
        """
        return (self.__str__())

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
