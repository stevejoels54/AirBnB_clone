#!/usr/bin/python3
"""Defines the amenity class tests"""
import unittest
from models.amenity import Amenity
from datetime import datetime
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Defines the Amenity class tests"""

    def setUp(self):
        self.amenity = Amenity()

    def test_inheritance(self):
        # Test if Amenity class inherits from BaseModel
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        # Test if Amenity has the required attributes
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_defaults(self):
        # Test if attributes have correct default values
        self.assertEqual(self.amenity.name, "")

    def test_str_representation(self):
        # Test if __str__ method returns a proper representation
        self.assertEqual(str(self.amenity),
                         "[Amenity] ({}) {}".format(self.amenity.id,
                                                    self.amenity.__dict__))

    def test_save_method(self):
        # Test if save() method updates updated_at attribute
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        new_updated_at = self.amenity.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        # Test if to_dict() method returns a dictionary with correct attributes
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)
        self.assertIsInstance(amenity_dict["id"], str)
        self.assertIsInstance(amenity_dict["name"], str)

    def test_to_dict_created_at_format(self):
        # Test if to_dict() method returns correct format for created_at
        amenity_dict = self.amenity.to_dict()
        created_at = datetime.strptime(amenity_dict["created_at"],
                                       "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(created_at, self.amenity.created_at)

    def test_to_dict_updated_at_format(self):
        # Test if to_dict() method returns correct format for updated_at
        amenity_dict = self.amenity.to_dict()
        updated_at = datetime.strptime(amenity_dict["updated_at"],
                                       "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated_at, self.amenity.updated_at)


if __name__ == '__main__':
    unittest.main()
