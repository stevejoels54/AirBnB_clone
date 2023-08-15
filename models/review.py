#!/usr/bin/python3
"""Defines a review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the review class. """

    place_id = ""
    user_id = ""
    text = ""
