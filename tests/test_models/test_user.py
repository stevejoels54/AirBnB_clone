#!/usr/bin/python3
"""User class user test cases."""

import unittest
from models.user import User
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """User class unit tests."""

    def setUp(self):
        self.user = User()

    def test_inheritance(self):
        # Test if User class inherits from BaseModel
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        # Test if User has the required attributes
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_defaults(self):
        # Test if attributes have correct default values
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str_representation(self):
        # Test if __str__ method returns a proper representation
        self.assertEqual(str(self.user),
                         "[User] ({}) {}".format(self.user.id,
                                                 self.user.__dict__))

    def test_save_method(self):
        # Test if save() method updates updated_at attribute
        old_updated_at = self.user.updated_at
        self.user.save()
        new_updated_at = self.user.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        # Test if to_dict() method returns a dictionary with correct attributes
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)
        self.assertIsInstance(user_dict["id"], str)
        self.assertIsInstance(user_dict["email"], str)
        self.assertIsInstance(user_dict["password"], str)
        self.assertIsInstance(user_dict["first_name"], str)
        self.assertIsInstance(user_dict["last_name"], str)

    def test_to_dict_created_at_format(self):
        # Test if to_dict() method returns correct format for created_at
        user_dict = self.user.to_dict()
        created_at = datetime.strptime(user_dict["created_at"],
                                       "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(created_at, self.user.created_at)

    def test_to_dict_updated_at_format(self):
        # Test if to_dict() method returns correct format for updated_at
        user_dict = self.user.to_dict()
        updated_at = datetime.strptime(user_dict["updated_at"],
                                       "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated_at, self.user.updated_at)


if __name__ == '__main__':
    unittest.main()
