#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestInstantiation
    TestSave
    TestTo_dict
"""
import datetime
import time
from models.review import Review
import models
import unittest
import os


class TestInstantiation(unittest.TestCase):
    """
    Unittests for review class Instantiation
    """

    def test_object_type(self):
        self.assertEqual(Review, type(Review()))

    def test_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_id_type(self):
        self.assertEqual(str, type(Review().id))

    def test_updated_at_type(self):
        self.assertEqual(datetime.datetime, type(Review().updated_at))

    def test_created_at_type(self):
        self.assertEqual(datetime.datetime, type(Review().created_at))

    def test_unique_ids(self):
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_different_created_dates(self):
        review1 = Review()
        time.sleep(0.1)
        review2 = Review()
        self.assertLess(review1.created_at, review2.created_at)

    def test_different_updated_dates(self):
        review1 = Review()
        time.sleep(0.1)
        review2 = Review()
        self.assertLess(review1.updated_at, review2.updated_at)

    def test_instance_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_place_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_user_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_text_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_str_representation(self):
        date = datetime.datetime.now()
        date_r = repr(date)
        review = Review()
        review.id = "5"
        review.created_at = review.updated_at = date
        amenity_str = review.__str__()
        self.assertIn("[Review] (5)", amenity_str)
        self.assertIn("'id': '5'", amenity_str)
        self.assertIn("'created_at': " + date_r, amenity_str)
        self.assertIn("'updated_at': " + date_r, amenity_str)

    def test_None_arg(self):
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def test_kwargs(self):
        date = datetime.datetime.now()
        iso_date = date.isoformat()
        review = Review(id="1", created_at=iso_date, updated_at=iso_date)
        self.assertEqual(review.id, "1")
        self.assertEqual(review.created_at, date)
        self.assertEqual(review.updated_at, date)


class TestSave(unittest.TestCase):
    """
    Unittests save method of the Review class.
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
        review = Review()
        time.sleep(0.1)
        old_updated_at = review.updated_at
        review.save()
        self.assertLess(old_updated_at, review.updated_at)

    def test_saves_twice(self):
        review = Review()
        time.sleep(0.1)
        old_updated_at = review.updated_at
        review.save()
        new_updated_at = review.updated_at
        self.assertLess(old_updated_at, new_updated_at)
        time.sleep(0.1)
        review.save()
        self.assertLess(new_updated_at, review.updated_at)

    def test_args(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.save(None)

    def test_updates_file(self):
        review = Review()
        review.save()
        amenity_id = "Review." + review.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())


class TestTo_dict(unittest.TestCase):
    """
    Unittests for to_dict method of the Review class.
    """

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_keys(self):
        review = Review()
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())
        self.assertIn("__class__", review.to_dict())

    def test_added_attributes(self):
        review = Review()
        review.name = "test"
        review.number = 12
        self.assertEqual("test", review.name)
        self.assertIn("number", review.to_dict())

    def test_attributes_types(self):
        review = Review()
        am_dict = review.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_output(self):
        date = datetime.datetime.now()
        review = Review()
        review.id = "5"
        review.created_at = review.updated_at = date
        dict_t = {
            'id': '5',
            '__class__': 'Review',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(review.to_dict(), dict_t)

    def test_dict_different(self):
        review = Review()
        self.assertNotEqual(review.to_dict(), review.__dict__)

    def test_args(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.to_dict(None)


if __name__ == "__main__":
    unittest.main()
