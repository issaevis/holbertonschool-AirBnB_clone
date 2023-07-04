#!/usr/bin/python3


import json
import os


class FileStorage:
    """Class to handle file storage"""
    def __init__(self):
        self.__file_path = "filezz.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = str(obj)

    def save(self):
        with open(self.__file_path, 'w') as outfile:
            outfile.write(json.dumps(self.__objects))

    def reload(self):
        if not os.path.exists(self.__file_path):
            return
        elif os.path.getsize(self.__file_path) == 0:
            return
        else:
            with open(self.__file_path, "r") as infile:
                self.__objects = json.loads(infile.read())

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        if not isinstance(value, str) or not os.path.exists(value):
            raise ValueError("Invalid path for the JSON data")
        else:
            self.__file_path = value
