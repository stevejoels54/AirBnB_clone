#!/usr/bin/python3
"""Defines the place class test cases."""

import unittest
from models.place import Place
from datetime import datetime
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test the place class"""

    def setUp(self):
        self.place = Place()

    def test_inheritance(self):
        # Test if Place class inherits from BaseModel
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        # Test if Place has the required attributes
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))

    def test_defaults(self):
        # Test if attributes have correct default values
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_str_representation(self):
        # Test if __str__ method returns a proper representation
        self.assertEqual(str(self.place),
                         "[Place] ({}) {}".format(self.place.id,
                                                  self.place.__dict__))

    def test_save_method(self):
        # Test if save() method updates updated_at attribute
        old_updated_at = self.place.updated_at
        self.place.save()
        new_updated_at = self.place.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        # Test if to_dict() method returns a dictionary with correct attributes
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertIsInstance(place_dict["created_at"], str)
        self.assertIsInstance(place_dict["updated_at"], str)
        self.assertIsInstance(place_dict["id"], str)
        self.assertIsInstance(place_dict["city_id"], str)
        self.assertIsInstance(place_dict["user_id"], str)
        self.assertIsInstance(place_dict["name"], str)
        self.assertIsInstance(place_dict["description"], str)
        self.assertIsInstance(place_dict["number_rooms"], int)
        self.assertIsInstance(place_dict["number_bathrooms"], int)
        self.assertIsInstance(place_dict["max_guest"], int)
        self.assertIsInstance(place_dict["price_by_night"], int)
        self.assertIsInstance(place_dict["latitude"], float)
        self.assertIsInstance(place_dict["longitude"], float)
        self.assertIsInstance(place_dict["amenity_ids"], list)

    def test_to_dict_created_at_format(self):
        # Test if to_dict() method returns correct format for created_at
        place_dict = self.place.to_dict()
        created_at = datetime.strptime(place_dict["created_at"],
                                       "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(created_at, self.place.created_at)

    def test_to_dict_updated_at_format(self):
        # Test if to_dict() method returns correct format for updated_at
        place_dict = self.place.to_dict()
        updated_at = datetime.strptime(place_dict["updated_at"],
                                       "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated_at, self.place.updated_at)


if __name__ == '__main__':
    unittest.main()
