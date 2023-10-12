#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestClass_instantiation
    TestFileStorage_methods
"""
import models
import unittest
import os
import shutil
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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
    def setUpClass(cls):
        try:
            shutil.copy2("file.json", "temp")
            FileStorage._FileStorage__file_path = "temp"
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("temp")
            FileStorage._FileStorage__file_path = "file.json"
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
        models.storage.save()
        with open("temp", "r") as f:
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


class TestWithUser(unittest.TestCase):
    """testing that FileStorage class correctly handles User class"""

    @classmethod
    def setUpClass(cls):
        try:
            shutil.copy2("file.json", "temp")
            FileStorage._FileStorage__file_path = "temp"
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("temp")
            FileStorage._FileStorage__file_path = "file.json"
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_new_method(self):
        obj = User()
        models.storage.new(obj)
        self.assertIn("User." + obj.id, models.storage.all().keys())
        self.assertIn(obj, models.storage.all().values())

    def test_save_method(self):
        obj = User()
        models.storage.new(obj)
        models.storage.save()
        with open("temp", "r") as f:
            storage_content = f.read()
            self.assertIn("User." + obj.id, storage_content)

    def test_reload_method(self):
        obj = User()
        key = "User." + obj.id
        obj.name = 'Link'

        models.storage.new(obj)
        models.storage.save()
        models.storage.reload()
        storage_objs = FileStorage._FileStorage__objects

        self.assertIn(key, storage_objs)
        self.assertEqual(storage_objs[key].id, obj.id)
        self.assertEqual(storage_objs[key].name, 'Link')


class TestWithState(unittest.TestCase):
    """testing that FileStorage class correctly handles State class"""

    @classmethod
    def setUpClass(cls):
        try:
            shutil.copy2("file.json", "temp")
            FileStorage._FileStorage__file_path = "temp"
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("temp")
            FileStorage._FileStorage__file_path = "file.json"
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_new_method(self):
        obj = State()
        models.storage.new(obj)
        self.assertIn("State." + obj.id, models.storage.all().keys())
        self.assertIn(obj, models.storage.all().values())

    def test_save_method(self):
        obj = State()
        models.storage.new(obj)
        models.storage.save()
        with open("temp", "r") as f:
            storage_content = f.read()
            self.assertIn("State." + obj.id, storage_content)

    def test_reload_method(self):
        obj = State()
        key = "State." + obj.id
        obj.name = 'California'

        models.storage.new(obj)
        models.storage.save()
        models.storage.reload()
        storage_objs = FileStorage._FileStorage__objects

        self.assertIn(key, storage_objs)
        self.assertEqual(storage_objs[key].id, obj.id)
        self.assertEqual(storage_objs[key].name, 'California')


class TestWithCity(unittest.TestCase):
    """testing that FileStorage class correctly handles City class"""

    @classmethod
    def setUpClass(cls):
        try:
            shutil.copy2("file.json", "temp")
            FileStorage._FileStorage__file_path = "temp"
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("temp")
            FileStorage._FileStorage__file_path = "file.json"
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_new_method(self):
        obj = City()
        models.storage.new(obj)
        self.assertIn("City." + obj.id, models.storage.all().keys())
        self.assertIn(obj, models.storage.all().values())

    def test_save_method(self):
        obj = City()
        models.storage.new(obj)
        models.storage.save()
        with open("temp", "r") as f:
            storage_content = f.read()
            self.assertIn("City." + obj.id, storage_content)

    def test_reload_method(self):
        obj = City()
        key = "City." + obj.id
        obj.name = 'Tokyo'

        models.storage.new(obj)
        models.storage.save()
        models.storage.reload()
        storage_objs = FileStorage._FileStorage__objects

        self.assertIn(key, storage_objs)
        self.assertEqual(storage_objs[key].id, obj.id)
        self.assertEqual(storage_objs[key].name, 'Tokyo')


class TestWithPlace(unittest.TestCase):
    """testing that FileStorage class correctly handles Place class"""

    @classmethod
    def setUpClass(cls):
        try:
            shutil.copy2("file.json", "temp")
            FileStorage._FileStorage__file_path = "temp"
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("temp")
            FileStorage._FileStorage__file_path = "file.json"
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_new_method(self):
        obj = Place()
        models.storage.new(obj)
        self.assertIn("Place." + obj.id, models.storage.all().keys())
        self.assertIn(obj, models.storage.all().values())

    def test_save_method(self):
        obj = Place()
        models.storage.new(obj)
        models.storage.save()
        with open("temp", "r") as f:
            storage_content = f.read()
            self.assertIn("Place." + obj.id, storage_content)

    def test_reload_method(self):
        obj = Place()
        key = "Place." + obj.id
        obj.name = 'Square Park'
        obj.max_guest = 5
        obj.latitude = 77.8
        obj.longitude = 45.23
        bathroom, kitchen, balcony = Amenity(), Amenity(), Amenity()
        list_amenity_ids = [bathroom.id, kitchen.id, balcony.id]
        obj.amenity_ids = list_amenity_ids

        models.storage.new(obj)
        models.storage.save()
        models.storage.reload()
        storage_objs = FileStorage._FileStorage__objects

        self.assertIn(key, storage_objs)

        self.assertEqual(type(storage_objs[key].id), str)
        self.assertEqual(storage_objs[key].id, obj.id)

        self.assertEqual(type(storage_objs[key].name), str)
        self.assertEqual(storage_objs[key].name, 'Square Park')

        self.assertEqual(type(storage_objs[key].max_guest), int)
        self.assertEqual(storage_objs[key].max_guest, 5)

        self.assertEqual(type(storage_objs[key].latitude), float)
        self.assertEqual(storage_objs[key].latitude, 77.8)

        self.assertEqual(type(storage_objs[key].longitude), float)
        self.assertEqual(storage_objs[key].longitude, 45.23)

        self.assertEqual(type(storage_objs[key].amenity_ids), list)
        self.assertEqual(storage_objs[key].amenity_ids, list_amenity_ids)


class TestWithAmenity(unittest.TestCase):
    """testing that FileStorage class correctly handles Amenity class"""

    @classmethod
    def setUpClass(cls):
        try:
            shutil.copy2("file.json", "temp")
            FileStorage._FileStorage__file_path = "temp"
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("temp")
            FileStorage._FileStorage__file_path = "file.json"
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_new_method(self):
        obj = Amenity()
        models.storage.new(obj)
        self.assertIn("Amenity." + obj.id, models.storage.all().keys())
        self.assertIn(obj, models.storage.all().values())

    def test_save_method(self):
        obj = Amenity()
        models.storage.new(obj)
        models.storage.save()
        with open("temp", "r") as f:
            storage_content = f.read()
            self.assertIn("Amenity." + obj.id, storage_content)

    def test_reload_method(self):
        obj = Amenity()
        key = "Amenity." + obj.id
        obj.name = 'Kitchen'

        models.storage.new(obj)
        models.storage.save()
        models.storage.reload()
        storage_objs = FileStorage._FileStorage__objects

        self.assertIn(key, storage_objs)
        self.assertEqual(storage_objs[key].id, obj.id)
        self.assertEqual(storage_objs[key].name, 'Kitchen')


class TestWithReview(unittest.TestCase):
    """testing that FileStorage class correctly handles Review class"""

    @classmethod
    def setUpClass(cls):
        try:
            shutil.copy2("file.json", "temp")
            FileStorage._FileStorage__file_path = "temp"
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("temp")
            FileStorage._FileStorage__file_path = "file.json"
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_new_method(self):
        obj = Review()
        models.storage.new(obj)
        self.assertIn("Review." + obj.id, models.storage.all().keys())
        self.assertIn(obj, models.storage.all().values())

    def test_save_method(self):
        obj = Review()
        models.storage.new(obj)
        models.storage.save()
        with open("temp", "r") as f:
            storage_content = f.read()
            self.assertIn("Review." + obj.id, storage_content)

    def test_reload_method(self):
        obj = Review()
        key = "Review." + obj.id
        obj.text = 'Excellent'

        models.storage.new(obj)
        models.storage.save()
        models.storage.reload()
        storage_objs = FileStorage._FileStorage__objects

        self.assertIn(key, storage_objs)
        self.assertEqual(storage_objs[key].id, obj.id)
        self.assertEqual(storage_objs[key].text, 'Excellent')


if __name__ == "__main__":
    unittest.main()
