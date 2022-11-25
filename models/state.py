#!/usr/bin/python3
"""This is a State class that Inherits from the BaseModel"""
from models.base_model import BaseModel

class State(BaseModel):
    """This is the State class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """This is the init method"""
        super().__init__(*args, **kwargs)