#!/usr/bin/python3SS
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Class to handle file storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns all objects stored in FileStorage'''
        return FileStorage.__objects

    def new(self, obj):
        '''saves a new object to FileStorage'''
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
        return True

    def save(self):
        '''saves objects to a JSON file'''
        with open(FileStorage.__file_path, 'w') as f:
            new_dict = {}
            x = self.all()
            for element in x:
                new_dict[element] = x[element].to_dict()
            f.write(json.dumps(new_dict))
        return True

    def reload(self):
        '''loads from JSON and creates object'''
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                content = f.read()
                if len(content) != 0:
                    obj = json.loads(content)
                    for key, value in obj.items():
                        value = eval(value['__class__'])(**value)
                        FileStorage.new(self, value)
        return True
    
    def file_path():
        return FileStorage.__file_path