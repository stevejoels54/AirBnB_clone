#!/usr/bin/python3
"""Defines a review class test cases"""

import unittest
from models.review import Review
from datetime import datetime
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Defines a review class test cases"""

    def setUp(self):
        self.review = Review()

    def test_inheritance(self):
        # Test if Review class inherits from BaseModel
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        # Test if Review has the required attributes
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_defaults(self):
        # Test if attributes have correct default values
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_str_representation(self):
        # Test if __str__ method returns a proper representation
        self.assertEqual(str(self.review),
                         "[Review] ({}) {}".format(self.review.id,
                                                   self.review.__dict__))

    def test_save_method(self):
        # Test if save() method updates updated_at attribute
        old_updated_at = self.review.updated_at
        self.review.save()
        new_updated_at = self.review.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        # Test if to_dict() method returns a dictionary with correct attributes
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)
        self.assertIsInstance(review_dict["id"], str)
        self.assertIsInstance(review_dict["place_id"], str)
        self.assertIsInstance(review_dict["user_id"], str)
        self.assertIsInstance(review_dict["text"], str)

    def test_to_dict_created_at_format(self):
        # Test if to_dict() method returns correct format for created_at
        review_dict = self.review.to_dict()
        created_at = datetime.strptime(review_dict["created_at"],
                                       "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(created_at, self.review.created_at)

    def test_to_dict_updated_at_format(self):
        # Test if to_dict() method returns correct format for updated_at
        review_dict = self.review.to_dict()
        updated_at = datetime.strptime(review_dict["updated_at"],
                                       "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated_at, self.review.updated_at)


if __name__ == '__main__':
    unittest.main()
