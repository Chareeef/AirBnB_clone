#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestInstantiation
    TestSave
    TestTo_dict
"""
import datetime
import time
from models.amenity import Amenity
import models
import unittest
import os


class TestInstantiation(unittest.TestCase):
    """
    Unittests for amenity class Instantiation
    """

    def test_object_type(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_id_type(self):
        self.assertEqual(str, type(Amenity().id))

    def test_updated_at_type(self):
        self.assertEqual(datetime.datetime, type(Amenity().updated_at))

    def test_created_at_type(self):
        self.assertEqual(datetime.datetime, type(Amenity().created_at))

    def test_unique_ids(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_different_created_dates(self):
        amenity1 = Amenity()
        time.sleep(0.1)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_different_updated_dates(self):
        amenity1 = Amenity()
        time.sleep(0.1)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_instance_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_name_type(self):
        amenity = Amenity()
        self.assertNotIn("name", amenity.__dict__)
        self.assertIn("name", dir(Amenity()))
        self.assertEqual(str, type(Amenity.name))

    def test_str_representation(self):
        date = datetime.datetime.now()
        date_r = repr(date)
        amenity = Amenity()
        amenity.id = "5"
        amenity.created_at = amenity.updated_at = date
        amenity_str = amenity.__str__()
        self.assertIn("[Amenity] (5)", amenity_str)
        self.assertIn("'id': '5'", amenity_str)
        self.assertIn("'created_at': " + date_r, amenity_str)
        self.assertIn("'updated_at': " + date_r, amenity_str)

    def test_None_arg(self):
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def test_kwargs(self):
        date = datetime.datetime.now()
        iso_date = date.isoformat()
        amenity = Amenity(id="1", created_at=iso_date, updated_at=iso_date)
        self.assertEqual(amenity.id, "1")
        self.assertEqual(amenity.created_at, date)
        self.assertEqual(amenity.updated_at, date)


class TestSave(unittest.TestCase):
    """
    Unittests save method of the Amenity class.
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save(self):
        amenity = Amenity()
        time.sleep(0.1)
        old_updated_at = amenity.updated_at
        amenity.save()
        self.assertLess(old_updated_at, amenity.updated_at)

    def test_saves_twice(self):
        amenity = Amenity()
        time.sleep(0.1)
        old_updated_at = amenity.updated_at
        amenity.save()
        new_updated_at = amenity.updated_at
        self.assertLess(old_updated_at, new_updated_at)
        time.sleep(0.1)
        amenity.save()
        self.assertLess(new_updated_at, amenity.updated_at)

    def test_args(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.save(None)

    def test_updates_file(self):
        amenity = Amenity()
        amenity.save()
        amenity_id = "Amenity." + amenity.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())


class TestTo_dict(unittest.TestCase):
    """
    Unittests for to_dict method of the Amenity class.
    """

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_keys(self):
        amenity = Amenity()
        self.assertIn("id", amenity.to_dict())
        self.assertIn("created_at", amenity.to_dict())
        self.assertIn("updated_at", amenity.to_dict())
        self.assertIn("__class__", amenity.to_dict())

    def test_added_attributes(self):
        amenity = Amenity()
        amenity.name = "test"
        amenity.number = 12
        self.assertEqual("test", amenity.name)
        self.assertIn("number", amenity.to_dict())

    def test_attributes_types(self):
        amenity = Amenity()
        am_dict = amenity.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_output(self):
        date = datetime.datetime.now()
        amenity = Amenity()
        amenity.id = "5"
        amenity.created_at = amenity.updated_at = date
        dict_t = {
            'id': '5',
            '__class__': 'Amenity',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(amenity.to_dict(), dict_t)

    def test_dict_different(self):
        amenity = Amenity()
        self.assertNotEqual(amenity.to_dict(), amenity.__dict__)

    def test_args(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.to_dict(None)


if __name__ == "__main__":
    unittest.main()
