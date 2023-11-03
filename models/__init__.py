#!/usr/bin/python3
"""
Module for init
"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

""" creates storage and reloads """
storage = FileStorage()
storage.reload()

classes = [
    "BaseModel",
    "User"
]
