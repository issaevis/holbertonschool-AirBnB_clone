#!/usr/bin/python3
'''BaseModel class to build on top of'''


from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self):
        '''inits the class'''
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''messes with the str return'''
        return (f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>")

    def save(self):
        '''changes the savedate'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''adds to a dict and returns it'''
        dictionary = self.__dict__
        setattr(self, "__class__", self.__class__.__name__)
        setattr(self, "created_at", self.created_at.isoformat())
        setattr(self, "updated_at", self.updated_at.isoformat())
        return dictionary
