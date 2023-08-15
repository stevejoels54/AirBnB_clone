#!/usr/bin/python3
"""Define city class tests"""

import unittest
from models.city import City
from datetime import datetime
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test the City class"""

    def setUp(self):
        self.city = City()

    def test_inheritance(self):
        # Test if City class inherits from BaseModel
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        # Test if City has the required attributes
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_defaults(self):
        # Test if attributes have correct default values
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_str_representation(self):
        # Test if __str__ method returns a proper representation
        self.assertEqual(str(self.city),
                         "[City] ({}) {}".format(self.city.id,
                                                 self.city.__dict__))

    def test_save_method(self):
        # Test if save() method updates updated_at attribute
        old_updated_at = self.city.updated_at
        self.city.save()
        new_updated_at = self.city.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        # Test if to_dict() method returns a dictionary with correct attributes
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)
        self.assertIsInstance(city_dict["id"], str)
        self.assertIsInstance(city_dict["state_id"], str)
        self.assertIsInstance(city_dict["name"], str)

    def test_to_dict_created_at_format(self):
        # Test if to_dict() method returns correct format for created_at
        city_dict = self.city.to_dict()
        created_at = datetime.strptime(city_dict["created_at"],
                                       "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(created_at, self.city.created_at)

    def test_to_dict_updated_at_format(self):
        # Test if to_dict() method returns correct format for updated_at
        city_dict = self.city.to_dict()
        updated_at = datetime.strptime(city_dict["updated_at"],
                                       "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated_at, self.city.updated_at)


if __name__ == '__main__':
    unittest.main()
