#!/usr/bin/python3
"""This class defines Amenity"""        
from models.base_model import BaseModel
class Amenity(BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    name = ""
    def __init__(self, *args, **kwargs):
        """This is the init method"""
        super().__init__(*args, **kwargs)