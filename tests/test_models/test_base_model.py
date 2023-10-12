#!/usr/bin/python3

"""Unittests for models/base_model.py

Test Classes:
    TestCreateFromDict
    TestModel_instantiation
    TestSave
    TestToDict
"""

import models
import os
from models.base_model import BaseModel
import datetime
import unittest
import time


class TestModel_instantiation(unittest.TestCase):
    """
    This Class tests instantiation of the base model class
    """

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_type(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_updated_at_type(self):
        self.assertEqual(datetime.datetime, type(BaseModel().updated_at))

    def test_created_at_type(self):
        self.assertEqual(datetime.datetime, type(BaseModel().created_at))

    def test_unique_ids(self):
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_different_created_dates(self):
        base_model1 = BaseModel()
        time.sleep(0.1)
        base_model2 = BaseModel()
        self.assertLess(base_model1.created_at, base_model2.created_at)

    def test_different_updated_dates(self):
        base_model1 = BaseModel()
        time.sleep(0.1)
        base_model2 = BaseModel()
        self.assertLess(base_model1.updated_at, base_model2.updated_at)

    def test_str_representation(self):
        today = datetime.datetime.today()
        today_representation = repr(today)
        base_model1 = BaseModel()
        base_model1.id = "5"
        base_model1.created_at = today
        base_model1.updated_at = today

        model_str = base_model1.__str__()
        self.assertIn("[BaseModel] (5)", model_str)
        self.assertIn("'id': '5'", model_str)
        self.assertIn("'created_at': " + today_representation, model_str)
        self.assertIn("'updated_at': " + today_representation, model_str)

    def test__args(self):
        base_model = BaseModel(None)
        self.assertNotIn(None, base_model.__dict__.values())

    def test_kwargs(self):
        date = datetime.datetime.now()
        isodate = date.isoformat()
        base_model = BaseModel(id="1", created_at=isodate, updated_at=isodate)
        self.assertEqual(base_model.id, "1")
        self.assertEqual(base_model.created_at, date)
        self.assertEqual(base_model.updated_at, date)

    def test_instance_in_storage(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_empty_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        date = datetime.datetime.now()
        diso = date.isoformat()
        base_model = BaseModel("5", id="1", created_at=diso, updated_at=diso)
        self.assertEqual(base_model.id, "1")
        self.assertEqual(base_model.created_at, date)
        self.assertEqual(base_model.updated_at, date)


class TestSave(unittest.TestCase):
    """
    Testing save method of the BaseModel class.
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
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
        base_model = BaseModel()
        time.sleep(0.1)
        old_updated_at = base_model.updated_at
        base_model.save()
        self.assertLess(old_updated_at, base_model.updated_at)

    def test_saving_twice(self):
        base_model = BaseModel()
        time.sleep(0.1)
        updated_at1 = base_model.updated_at
        base_model.save()
        updated_at2 = base_model.updated_at
        self.assertLess(updated_at1, updated_at2)
        time.sleep(0.05)
        base_model.save()
        self.assertLess(updated_at2, base_model.updated_at)

    def test_args(self):
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.save(None)

    def test_storage_file(self):
        base_model = BaseModel()
        base_model.save()
        base_model_id = "BaseModel." + base_model.id
        with open("file.json", "r") as f:
            self.assertIn(base_model_id, f.read())


class TestToDict(unittest.TestCase):
    """
    Testing to_dict method of the BaseModel class.
    """

    def test_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_dict_keys(self):
        base_model = BaseModel()
        self.assertIn("__class__", base_model.to_dict())
        self.assertIn("id", base_model.to_dict())
        self.assertIn("created_at", base_model.to_dict())
        self.assertIn("updated_at", base_model.to_dict())

    def test_dict_contains_attribs(self):
        base_model = BaseModel()
        base_model.name = "Test"
        base_model.number = 5
        self.assertIn("name", base_model.to_dict())
        self.assertIn("number", base_model.to_dict())

    def test_values_types(self):
        base_model = BaseModel()
        base_dict = base_model.to_dict()
        self.assertEqual(str, type(base_dict["created_at"]))
        self.assertEqual(str, type(base_dict["updated_at"]))

    def test_dict_format(self):
        dt = datetime.datetime.now()
        base_model = BaseModel()
        base_model.id = "1"
        base_model.created_at = base_model.updated_at = dt
        dictt = {
            'id': '1',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(base_model.to_dict(), dictt)

    def test_args(self):
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.to_dict(None)

    def test_original_dict(self):
        base_model = BaseModel()
        self.assertNotEqual(base_model.to_dict(), base_model.__dict__)


class TestCreateFromDict(unittest.TestCase):
    '''
    This class tests different aspects when creating a BaseModel
    instance by passing a dictionary to its __init__ function
    '''

    def setUp(self):
        '''Runs before every test function'''
        self.b1 = BaseModel()
        self.b1.name = 'Stellar BaseModel'
        self.b1.category = 'Dwarf'
        self.b1.magnitude = 3.6
        self.b1.save()
        dict_b1 = self.b1.to_dict()

        self.b2 = BaseModel(**dict_b1)

    def test_b2_attributes(self):
        '''Test that b2 has the correct attributes'''

        b1, b2 = self.b1, self.b2

        self.assertEqual(b2.id, b1.id)
        self.assertEqual(b2.created_at, b1.created_at)
        self.assertEqual(b2.updated_at, b1.updated_at)
        self.assertEqual(b2.name, 'Stellar BaseModel')
        self.assertEqual(b2.category, 'Dwarf')
        self.assertEqual(b2.magnitude, 3.6)

        self.assertNotIn('__class__', b2.__dict__)

    def test_correct_types(self):
        '''Test that attributes have the right types'''

        b2 = self.b2

        self.assertIs(type(b2), BaseModel)
        self.assertIs(type(b2.id), str)
        self.assertIs(type(b2.created_at), datetime.datetime)
        self.assertIs(type(b2.updated_at), datetime.datetime)
        self.assertIs(type(b2.name), str)
        self.assertIs(type(b2.category), str)
        self.assertIs(type(b2.magnitude), float)

    def test_difference_between_instances(self):
        '''Test that attributes we really have different instances'''

        b1, b2 = self.b1, self.b2

        self.assertIsNot(b1, b2)

        b2.save()
        self.assertEqual(b2.created_at, b1.created_at)
        self.assertNotEqual(b2.updated_at, b1.updated_at)


if __name__ == "__main__":
    unittest.main()
