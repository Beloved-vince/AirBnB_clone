#!/usr/bin/python3
"""This module contains the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines the user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
