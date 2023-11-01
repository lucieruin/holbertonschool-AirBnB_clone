#!/usr/bin/python3
""" Module for serializing and deserializing instances and JSON files """


from models.base_model import BaseModel
import json


class FileStorage:
    """ defines FileStorage class """

    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """ defines __objects """
        return self.__objects

    def new(self, obj):
        """ sets obj in __objects with key/value pair """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    
    def save(self):
        """ serializes __objects to the JSON file """
        full_dict = {}
        for keys, value in self.__objects.items():
            full_dict[keys] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(full_dict, file, indent=4)

    def reload(self):
        """ reload method """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                temp_reload = json.load(file)
                for keys, value in temp_reload.items(): 
                    class_name, obj_id = keys.split(".")
                    instance = eval(class_name)(**value)
                    self.__objects[keys] = instance
        except FileNotFoundError:
            pass
