#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestInstantiation
    TestSave
    TestTo_dict
"""
import datetime
import time
from models.city import City
import models
import unittest
import os


class TestInstantiation(unittest.TestCase):
    """
    Unittests for city class Instantiation
    """

    def test_object_type(self):
        self.assertEqual(City, type(City()))

    def test_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_id_type(self):
        self.assertEqual(str, type(City().id))

    def test_updated_at_type(self):
        self.assertEqual(datetime.datetime, type(City().updated_at))

    def test_created_at_type(self):
        self.assertEqual(datetime.datetime, type(City().created_at))

    def test_unique_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_state_id_is_public_class_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_is_public_class_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_different_created_dates(self):
        city1 = City()
        time.sleep(0.1)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_different_updated_dates(self):
        city1 = City()
        time.sleep(0.1)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_instance_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_str_representation(self):
        date = datetime.datetime.now()
        date_r = repr(date)
        city = City()
        city.id = "5"
        city.created_at = city.updated_at = date
        amenity_str = city.__str__()
        self.assertIn("[City] (5)", amenity_str)
        self.assertIn("'id': '5'", amenity_str)
        self.assertIn("'created_at': " + date_r, amenity_str)
        self.assertIn("'updated_at': " + date_r, amenity_str)

    def test_None_arg(self):
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_kwargs(self):
        date = datetime.datetime.now()
        iso_date = date.isoformat()
        city = City(id="1", created_at=iso_date, updated_at=iso_date)
        self.assertEqual(city.id, "1")
        self.assertEqual(city.created_at, date)
        self.assertEqual(city.updated_at, date)


class TestSave(unittest.TestCase):
    """
    Unittests save method of the City class.
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
        city = City()
        time.sleep(0.1)
        old_updated_at = city.updated_at
        city.save()
        self.assertLess(old_updated_at, city.updated_at)

    def test_saves_twice(self):
        city = City()
        time.sleep(0.1)
        old_updated_at = city.updated_at
        city.save()
        new_updated_at = city.updated_at
        self.assertLess(old_updated_at, new_updated_at)
        time.sleep(0.1)
        city.save()
        self.assertLess(new_updated_at, city.updated_at)

    def test_args(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    def test_updates_file(self):
        city = City()
        city.save()
        amenity_id = "City." + city.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())


class TestTo_dict(unittest.TestCase):
    """
    Unittests for to_dict method of the City class.
    """

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_keys(self):
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())

    def test_added_attributes(self):
        city = City()
        city.name = "test"
        city.number = 12
        self.assertEqual("test", city.name)
        self.assertIn("number", city.to_dict())

    def test_attributes_types(self):
        city = City()
        am_dict = city.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_output(self):
        date = datetime.datetime.now()
        city = City()
        city.id = "5"
        city.created_at = city.updated_at = date
        dict_t = {
            'id': '5',
            '__class__': 'City',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(city.to_dict(), dict_t)

    def test_dict_different(self):
        city = City()
        self.assertNotEqual(city.to_dict(), city.__dict__)

    def test_args(self):
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)


if __name__ == "__main__":
    unittest.main()
