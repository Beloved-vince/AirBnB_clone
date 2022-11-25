#!/usr/bin/python3
"""This module contains the review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """This class defines a Review object"""
    place_id = ""
    user_id = ""
    text = ""