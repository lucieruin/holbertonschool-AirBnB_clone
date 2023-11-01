#!/usr/bin/python3
""" Module for serializing and deserializing instances and JSON files """


import os
import json


class FileStorage:
    """ defines FileStorage class """

    __file_path = "./file.json"
    __objects = {}

    """ defines __objects """
    def all(self):
        return self.__objects

    """ sets obj in __objects with key/value pair """
    def new(self, obj):
        self.__objects = {obj.id: obj}

    """ serializes __objects to the JSON file """
    def save(self):
        full_dict = {}
        for keys, value in self.__objects.items():
            full_dict[keys] = value.to_dict()
        with open(self.__file_path, "w", encoding="UTF-8") as file:
            json.dump(full_dict, file, indent= 4)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as file:
                temp_reload = (json.load(file))
                for keys, value in temp_reload.items(): 
                    class_name, obj_id = keys.split(".")
                    instance = eval(class_name)(**value)
                    self.__objects[keys] = instance
        except FileNotFoundError:
            pass
