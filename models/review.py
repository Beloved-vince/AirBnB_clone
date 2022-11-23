#!!/usr/bin/python3
"""This class defines a Review"""
from models.base_model import BaseModel
class Review(BaseModel):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    place_id = ""
    user_id = ""
    text = ""
   