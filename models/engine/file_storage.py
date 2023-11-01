#!/usr/bin/python3
"""
Module for serializing and deserializing instances and JSON files
"""


import os
import json


class FileStorage:
    """ defines FileStorage class """

    __file_path = "../../file.json"
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
        with open(self.__file_path, "w", encoding="UTF-8") as file:

            for index in self.__objects.keys():
                temp = (self.__objects[index]).to_json()
                full_dict[index] = temp
            file.write(json.dumps(full_dict))

    """ deserializes the JSON file to __objects """
    def reload(self):
        try:
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, "r", encoding="UTF-8") as file:
                    temp_reload = (json.load(file))
                    for index in temp_reload.keys():
                        self.__objects[index] = dict(temp_reload[index]) #need to somehow convert 
                        return(self.__objects)
        except Exception as e:
            print (e)
