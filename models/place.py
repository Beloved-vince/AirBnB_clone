#!/usr/bin/python3
"""This class defines a Place"""
from models.base_model import BaseModel
class Place(BaseModel):
    """This is the class for Place
    Attributes:
        city_id: The city id
        user_id: The user id
        name: input name
        description: description of place
        number_rooms: number of rooms
        number_bathrooms: number of bathrooms
        max_guest: max number of guests
        price_by_night: price per night
        latitude: latitude
        longitude: longitude
        amenity_ids: list of Amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
  