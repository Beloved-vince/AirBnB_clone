#!/usr/bin/python3
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
