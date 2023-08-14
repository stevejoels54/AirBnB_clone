#!usr/bin/python3
"""Definition of the BaseModel class."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel class.

        Args:
            self (BaseModel): current instance
            args (any): never used
            kwargs (dict): dictionary of key/value pairs attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs):
            iso_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, iso_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
            """Return string representation of instance."""
            return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary with all
            keys/values of __dict__ of the instance."""
        new_dic = self.__dict__.copy()
        new_dic["created_at"] = self.created_at.isoformat()
        new_dic["updated_at"] = self.updated_at.isoformat()
        new_dic["__class__"] = self.__class__.__name__

        return new_dic
