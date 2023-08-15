#!/usr/bin/python3
"""Definition of the BaseModel test cases"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage(file_path=self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        # Test if all() method returns the correct dictionary
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        # Test if new() method adds an object to the dictionary
        user = User()
        self.storage.new(user)
        self.assertTrue(len(self.storage.all()) == 1)

    def test_save_reload(self):
        # Test if save() and reload() methods work correctly
        user = User()
        self.storage.new(user)
        self.storage.save()
        new_storage = FileStorage(file_path=self.file_path)
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertTrue(len(all_objs) == 1)

    def test_reload_nonexistent_file(self):
        # Test reload() when the file doesn't exist
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertEqual(all_objs, {})


if __name__ == '__main__':
    unittest.main()
