#!/usr/bin/python3


from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at


    def __str__(self):
        return (f"[{self.name}] ({self.id}) <{self.__dict__}>")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dictionary = self.__dict__
        setattr(self, "__class__", self.__class__)
        setattr(self, "created_at", self.created_at.isoformat())
        setattr(self, "updated_at", self.updated_at.isoformat())
        return dictionary

