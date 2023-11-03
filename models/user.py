#!/usr/bin/python3
""" user module """


from models.base_model import BaseModel


class User(BaseModel):
    """ class user """

    email = str("")
    password = str("")
    first_name = str("")
    last_name = str("")
