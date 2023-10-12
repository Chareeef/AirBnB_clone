#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestInstantiation
    TestSave
    TestTo_dict
"""
import datetime
import time
from models.state import State
import models
import unittest
import os


class TestInstantiation(unittest.TestCase):
    """
    Unittests for state class Instantiation
    """

    def test_object_type(self):
        self.assertEqual(State, type(State()))

    def test_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_id_type(self):
        self.assertEqual(str, type(State().id))

    def test_updated_at_type(self):
        self.assertEqual(datetime.datetime, type(State().updated_at))

    def test_created_at_type(self):
        self.assertEqual(datetime.datetime, type(State().created_at))

    def test_unique_ids(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_different_created_dates(self):
        state1 = State()
        time.sleep(0.1)
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def test_different_updated_dates(self):
        state1 = State()
        time.sleep(0.1)
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_instance_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_name_type(self):
        state = State()
        self.assertNotIn("name", state.__dict__)
        self.assertIn("name", dir(State()))
        self.assertEqual(str, type(State.name))

    def test_str_representation(self):
        date = datetime.datetime.now()
        date_r = repr(date)
        state = State()
        state.id = "5"
        state.created_at = state.updated_at = date
        amenity_str = state.__str__()
        self.assertIn("[State] (5)", amenity_str)
        self.assertIn("'id': '5'", amenity_str)
        self.assertIn("'created_at': " + date_r, amenity_str)
        self.assertIn("'updated_at': " + date_r, amenity_str)

    def test_None_arg(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_kwargs(self):
        date = datetime.datetime.now()
        iso_date = date.isoformat()
        state = State(id="1", created_at=iso_date, updated_at=iso_date)
        self.assertEqual(state.id, "1")
        self.assertEqual(state.created_at, date)
        self.assertEqual(state.updated_at, date)


class TestSave(unittest.TestCase):
    """
    Unittests save method of the State class.
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
        state = State()
        time.sleep(0.1)
        old_updated_at = state.updated_at
        state.save()
        self.assertLess(old_updated_at, state.updated_at)

    def test_saves_twice(self):
        state = State()
        time.sleep(0.1)
        old_updated_at = state.updated_at
        state.save()
        new_updated_at = state.updated_at
        self.assertLess(old_updated_at, new_updated_at)
        time.sleep(0.1)
        state.save()
        self.assertLess(new_updated_at, state.updated_at)

    def test_args(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)

    def test_updates_file(self):
        state = State()
        state.save()
        amenity_id = "State." + state.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())


class TestTo_dict(unittest.TestCase):
    """
    Unittests for to_dict method of the State class.
    """

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_keys(self):
        state = State()
        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("__class__", state.to_dict())

    def test_added_attributes(self):
        state = State()
        state.name = "test"
        state.number = 12
        self.assertEqual("test", state.name)
        self.assertIn("number", state.to_dict())

    def test_attributes_types(self):
        state = State()
        am_dict = state.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_output(self):
        date = datetime.datetime.now()
        state = State()
        state.id = "5"
        state.created_at = state.updated_at = date
        dict_t = {
            'id': '5',
            '__class__': 'State',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(state.to_dict(), dict_t)

    def test_dict_different(self):
        state = State()
        self.assertNotEqual(state.to_dict(), state.__dict__)

    def test_args(self):
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)


if __name__ == "__main__":
    unittest.main()
