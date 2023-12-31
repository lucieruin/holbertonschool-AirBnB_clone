#!/usr/bin/python3
""" the base model class """

from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ common attributes & methods """
    def __init__(self, *args, **kwargs):
        """ initialization method """
        if kwargs:
            for key, mydate in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    mydate = datetime.strptime(mydate, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, mydate)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """ print object """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ update the public instance attribute """
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
