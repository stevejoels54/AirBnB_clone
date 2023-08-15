#!/usr/bin/python3
"""Defines the state class test cases"""

import unittest
from models.state import State
from datetime import datetime
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the state class"""

    def setUp(self):
        self.state = State()

    def test_inheritance(self):
        # Test if State class inherits from BaseModel
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        # Test if State has the required attributes
        self.assertTrue(hasattr(self.state, "name"))
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_defaults(self):
        # Test if attributes have correct default values
        self.assertEqual(self.state.name, "")

    def test_str_representation(self):
        # Test if __str__ method returns a proper representation
        self.assertEqual(str(self.state),
                         "[State] ({}) {}".format(self.state.id,
                                                  self.state.__dict__))

    def test_save_method(self):
        # Test if save() method updates updated_at attribute
        old_updated_at = self.state.updated_at
        self.state.save()
        new_updated_at = self.state.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        # Test if to_dict() method returns a dictionary with correct attributes
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)
        self.assertIsInstance(state_dict["id"], str)
        self.assertIsInstance(state_dict["name"], str)

    def test_to_dict_created_at_format(self):
        # Test if to_dict() method returns correct format for created_at
        state_dict = self.state.to_dict()
        created_at = datetime.strptime(state_dict["created_at"],
                                       "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(created_at, self.state.created_at)

    def test_to_dict_updated_at_format(self):
        # Test if to_dict() method returns correct format for updated_at
        state_dict = self.state.to_dict()
        updated_at = datetime.strptime(state_dict["updated_at"],
                                       "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated_at, self.state.updated_at)


if __name__ == '__main__':
    unittest.main()
