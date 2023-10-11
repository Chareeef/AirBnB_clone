#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestClass_instantiation
    TestFileStorage_methods
"""
import models
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestClass_instantiation(unittest.TestCase):
    """Testing class instantiation"""

    def test_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_attribute_filepath_type(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_attribute_objects_type(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_models_storage(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestMethods(unittest.TestCase):
    """testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_method_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_method(self):
        base_m = BaseModel()
        models.storage.new(base_m)
        self.assertIn("BaseModel." + base_m.id, models.storage.all().keys())
        self.assertIn(base_m, models.storage.all().values())

    def test_new_method_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), "testing")

    def test_save_method(self):
        base_m = BaseModel()
        models.storage.new(base_m)
        with open("file.json", "r") as f:
            storage_content = f.read()
            self.assertIn("BaseModel." + base_m.id, storage_content)

    def test_save_method_args(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_method(self):
        base_m = BaseModel()
        models.storage.new(base_m)
        models.storage.save()
        models.storage.reload()
        storage_objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_m.id, storage_objs)

    def test_reload_method_args(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
