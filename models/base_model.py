#!/usr/bin/python3
'''BaseModel class to build on top of'''
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    '''Base model class that creates basemodel instances'''

    def __init__(self, *args, **kwargs):
        '''inits the class'''
        if not self.__dict__:
            if kwargs:
                for key, value in kwargs.items():
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    if key != "__class__":
                        setattr(self, key, value)
            else:
                self.id = str(uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                models.storage.new(self)

    def __str__(self):
        string = "[{}]".format(self.__class__.__name__)
        string += " ({}) {}".format(self.id, self.__dict__)
        return string

    def save(self):
        '''changes the savedate'''
        self.updated_at = datetime.utcnow()
        models.storage.save()
        return self.updated_at

    def to_dict(self):
        '''dict representation'''
        new_d = {}
        new_d = self.__dict__.copy()
        new_d["__class__"] = str(self.__class__.__name__)
        new_d['created_at'] = self.created_at.isoformat()
        new_d['updated_at'] = self.updated_at.isoformat()
        return new_d
