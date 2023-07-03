#!/usr/bin/python3
'''BaseModel class to build on top of'''


from uuid import uuid4
from datetime import datetime
from . import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        '''inits the class'''
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime
                            (value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    pass  # ignore this one, for the moment at least
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''messes with the str return'''
        return (f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>")

    def save(self):
        '''changes the savedate'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''adds to a dict and returns it'''
        dictionary = self.__dict__
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        return dictionary
