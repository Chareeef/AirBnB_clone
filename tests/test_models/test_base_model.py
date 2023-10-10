#!/usr/bin/python3

from models.base_model import BaseModel
import datetime
import unittest


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
