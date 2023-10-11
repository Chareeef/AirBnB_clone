#!/usr/bin/python3
"""This module implements the BaseModel class"""
import models
import datetime
import uuid


class BaseModel:
    """
    The BaseModel class

    Public instance attributes:
        id (uuid4)
        created_at (datetime)
        updated_at (datetime)

    Public instance methods:
        save(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel object.

        Args:
            *args (any): won't be used.
            **kwargs (dict): non-empty Key/value pairs of attributes.
        """

        if len(kwargs) != 0:
            frmt = "%Y-%m-%dT%H:%M:%S.%f"
            for key, val in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.datetime.strptime(val, frmt)
                elif key != "__class__":
                    self.__dict__[key] = val
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates `updated_at` with the current datetime"""

        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing:
            - All keys/values of __dict__ of the instance
            - The key __class__ with the class name of the object
        """

        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()

        return obj_dict

    def __str__(self):
        """Return a human readable representation of the instance"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
