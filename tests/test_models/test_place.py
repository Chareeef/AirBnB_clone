#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestInstantiation
    TestSave
    TestTo_dict
"""
import datetime
import time
from models.place import Place
import models
import unittest
import os


class TestInstantiation(unittest.TestCase):
    """
    Unittests for place class Instantiation
    """

    def test_object_type(self):
        self.assertEqual(Place, type(Place()))

    def test_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_id_type(self):
        self.assertEqual(str, type(Place().id))

    def test_updated_at_type(self):
        self.assertEqual(datetime.datetime, type(Place().updated_at))

    def test_created_at_type(self):
        self.assertEqual(datetime.datetime, type(Place().created_at))

    def test_unique_ids(self):
        review1 = Place()
        review2 = Place()
        self.assertNotEqual(review1.id, review2.id)

    def test_different_created_dates(self):
        review1 = Place()
        time.sleep(0.1)
        review2 = Place()
        self.assertLess(review1.created_at, review2.created_at)

    def test_different_updated_dates(self):
        review1 = Place()
        time.sleep(0.1)
        review2 = Place()
        self.assertLess(review1.updated_at, review2.updated_at)

    def test_instance_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_city_id_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_user_id_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

    def test_name_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)

    def test_description_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pl))
        self.assertNotIn("desctiption", pl.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pl))
        self.assertNotIn("number_rooms", pl.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pl))
        self.assertNotIn("price_by_night", pl.__dict__)

    def test_latitude_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pl))
        self.assertNotIn("latitude", pl.__dict__)

    def test_longitude_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pl))
        self.assertNotIn("longitude", pl.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pl))
        self.assertNotIn("amenity_ids", pl.__dict__)

    def test_str_representation(self):
        date = datetime.datetime.now()
        date_r = repr(date)
        place = Place()
        place.id = "5"
        place.created_at = place.updated_at = date
        amenity_str = place.__str__()
        self.assertIn("[Place] (5)", amenity_str)
        self.assertIn("'id': '5'", amenity_str)
        self.assertIn("'created_at': " + date_r, amenity_str)
        self.assertIn("'updated_at': " + date_r, amenity_str)

    def test_None_arg(self):
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_kwargs(self):
        date = datetime.datetime.now()
        iso_date = date.isoformat()
        place = Place(id="1", created_at=iso_date, updated_at=iso_date)
        self.assertEqual(place.id, "1")
        self.assertEqual(place.created_at, date)
        self.assertEqual(place.updated_at, date)


class TestSave(unittest.TestCase):
    """
    Unittests save method of the Place class.
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
        place = Place()
        time.sleep(0.1)
        old_updated_at = place.updated_at
        place.save()
        self.assertLess(old_updated_at, place.updated_at)

    def test_saves_twice(self):
        place = Place()
        time.sleep(0.1)
        old_updated_at = place.updated_at
        place.save()
        new_updated_at = place.updated_at
        self.assertLess(old_updated_at, new_updated_at)
        time.sleep(0.1)
        place.save()
        self.assertLess(new_updated_at, place.updated_at)

    def test_args(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.save(None)

    def test_updates_file(self):
        place = Place()
        place.save()
        amenity_id = "Place." + place.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())


class TestTo_dict(unittest.TestCase):
    """
    Unittests for to_dict method of the Place class.
    """

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_keys(self):
        place = Place()
        self.assertIn("id", place.to_dict())
        self.assertIn("created_at", place.to_dict())
        self.assertIn("updated_at", place.to_dict())
        self.assertIn("__class__", place.to_dict())

    def test_added_attributes(self):
        place = Place()
        place.name = "test"
        place.number = 12
        self.assertEqual("test", place.name)
        self.assertIn("number", place.to_dict())

    def test_attributes_types(self):
        place = Place()
        am_dict = place.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_output(self):
        date = datetime.datetime.now()
        place = Place()
        place.id = "5"
        place.created_at = place.updated_at = date
        dict_t = {
            'id': '5',
            '__class__': 'Place',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(place.to_dict(), dict_t)

    def test_dict_different(self):
        place = Place()
        self.assertNotEqual(place.to_dict(), place.__dict__)

    def test_args(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.to_dict(None)


if __name__ == "__main__":
    unittest.main()
