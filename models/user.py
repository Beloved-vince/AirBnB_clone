#!/usr/bin/python3
"""This module contains the user class"""
from models.base_model import BaseModel
from models import storage

class User(BaseModel):
    """This class defines the user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""



if __name__ == "__main__":
    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new User --")
    my_user = User()
    my_user.first_name = "Betty"
    my_user.last_name = "Bar"
    my_user.email = "airbnb@mail.com"
    my_user.password = "root"
    my_user.save()
    print(my_user)
    

    print("-- Create a new User 2 --")
    my_user2 = User()
    my_user2.first_name = "John"
    my_user2.email = "airbnb2@mail.com"
    my_user.password   = "root"
    my_user2.save()
    print(my_user2)

