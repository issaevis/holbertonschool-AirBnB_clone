#!/usr/bin/python3


import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Class to handle file storage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key in FileStorage.__objects:
            new_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as outfile:
            json.dump(new_dict, outfile)

    def reload(self):
        if not os.path.exists(FileStorage.__file_path):
            return
        elif os.path.getsize(FileStorage.__file_path) == 0:
            return
        else:
            with open(FileStorage.__file_path, "r") as infile:
                for key, value in json.load(infile).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value