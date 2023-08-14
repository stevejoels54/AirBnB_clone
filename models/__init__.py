#!/usr/bin/python3
"""FileStorage instance to use in app"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
