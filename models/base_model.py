#!/usr/bin/python3
'''BaseModel class to build on top of'''


from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        '''inits the class'''
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime
                            (value, "%Y-%m-%dT%H:%M:%S.%f"))
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''messes with the str return'''
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        '''changes the savedate'''
        self.updated_at = datetime.now()
        models.storage.save()
        return self.updated_at

    def to_dict(self):
        '''adds to a dict and returns it'''
        dictionary = self.__dict__.copy()
        print(type(dictionary["updated_at"]))
        dictionary["__class__"] = str(self.__class__.__name__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
