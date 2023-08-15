#!/usr/bin/python3
"""Definition of the BaseModel class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Class to serialize instances to a JSON file
    and deserialize JSON file to instances

    Attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store
        all objects by <class name>.id
    """

    def __init__(self, file_path="file.json"):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """
        Returns the dictionary of objects

        Returns:
            dictionary - dictionary of objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets the obj in the dictionary of objects with key <obj class name>.id

        Args:
            obj: object - object to be stored
        """
        class_name = obj.__class__.__name__
        id = obj.id
        self.__objects[class_name + "." + str(id)] = obj

    def save(self):
        """
        Serializes the dictionary of objects to the JSON file
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to the dictionary of objects
        """
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
            for key, value in self.__objects.items():
                class_name = key.split(".")[0]
                self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
