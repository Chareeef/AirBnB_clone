#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestInstantiation
    TestSave
    TestTo_dict
"""
import datetime
import time
from models.user import User
import models
import unittest
import os


class TestInstantiation(unittest.TestCase):
    """
    Unittests for user class Instantiation
    """

    def test_object_type(self):
        self.assertEqual(User, type(User()))

    def test_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_id_type(self):
        self.assertEqual(str, type(User().id))

    def test_updated_at_type(self):
        self.assertEqual(datetime.datetime, type(User().updated_at))

    def test_created_at_type(self):
        self.assertEqual(datetime.datetime, type(User().created_at))

    def test_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_different_created_dates(self):
        user1 = User()
        time.sleep(0.1)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_different_updated_dates(self):
        user1 = User()
        time.sleep(0.1)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_instance_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_str_representation(self):
        date = datetime.datetime.now()
        date_r = repr(date)
        user = User()
        user.id = "5"
        user.created_at = user.updated_at = date
        amenity_str = user.__str__()
        self.assertIn("[User] (5)", amenity_str)
        self.assertIn("'id': '5'", amenity_str)
        self.assertIn("'created_at': " + date_r, amenity_str)
        self.assertIn("'updated_at': " + date_r, amenity_str)

    def test_None_arg(self):
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_kwargs(self):
        date = datetime.datetime.now()
        iso_date = date.isoformat()
        user = User(id="1", created_at=iso_date, updated_at=iso_date)
        self.assertEqual(user.id, "1")
        self.assertEqual(user.created_at, date)
        self.assertEqual(user.updated_at, date)


class TestSave(unittest.TestCase):
    """
    Unittests save method of the User class.
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
        user = User()
        time.sleep(0.1)
        old_updated_at = user.updated_at
        user.save()
        self.assertLess(old_updated_at, user.updated_at)

    def test_saves_twice(self):
        user = User()
        time.sleep(0.1)
        old_updated_at = user.updated_at
        user.save()
        new_updated_at = user.updated_at
        self.assertLess(old_updated_at, new_updated_at)
        time.sleep(0.1)
        user.save()
        self.assertLess(new_updated_at, user.updated_at)

    def test_args(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_updates_file(self):
        user = User()
        user.save()
        amenity_id = "User." + user.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())


class TestTo_dict(unittest.TestCase):
    """
    Unittests for to_dict method of the User class.
    """

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_keys(self):
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_added_attributes(self):
        user = User()
        user.name = "test"
        user.number = 12
        self.assertEqual("test", user.name)
        self.assertIn("number", user.to_dict())

    def test_attributes_types(self):
        user = User()
        am_dict = user.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_output(self):
        date = datetime.datetime.now()
        user = User()
        user.id = "5"
        user.created_at = user.updated_at = date
        dict_t = {
            'id': '5',
            '__class__': 'User',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(user.to_dict(), dict_t)

    def test_dict_different(self):
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)

    def test_args(self):
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)

if __name__ == "__main__":
    unittest.main()
