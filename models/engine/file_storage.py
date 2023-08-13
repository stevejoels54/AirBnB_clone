#!usr/bin/python3
"""Definition of the BaseModel class."""
import json
from models.base_model import BaseModel


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
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        Deserializes the JSON file to the dictionary of objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
