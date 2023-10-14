#!/usr/bin/python3

"""Unittests for console

Test Classes:
    TestOrdinaryCommands
    TestCreateCommand
    TestShowCommand
    TestDestroyCommand
"""

import unittest
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class TestOrdinaryCommands(unittest.TestCase):
    """
    Unittests the typical console commands
    """

    def test_quit(self):
        '''Test the `quit` command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('quit')
            output = f.getvalue()
            self.assertEqual(output, '')

    def test_EOF(self):
        '''Test the `EOF` command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('EOF')
            output = f.getvalue()
            self.assertEqual(output, '')

    def test_help(self):
        '''Test the `help` command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help quit')
            output = f.getvalue().strip()
            self.assertEqual(output, HBNBCommand.do_quit.__doc__)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help EOF')
            output = f.getvalue().strip().strip()
            self.assertEqual(output, HBNBCommand.do_EOF.__doc__)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help help')
            output = f.getvalue().strip()
            self.assertEqual(output, HBNBCommand.do_help.__doc__)

    def test_emptyline(self):
        '''Test empty command line'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('')
            output = f.getvalue()
            self.assertEqual(output, '')


class TestCreateCommand(unittest.TestCase):
    """
    Unittests the `create` command
    """

    def setUp(self):
        '''Runs before every test'''

        self.storage = FileStorage()
        self.storage.reload()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        '''Runs after each test'''

        self.storage._Filestorage__objects = {}

    def test_errors(self):
        '''Test Errors mangement of `create` command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create')
            output = f.getvalue().strip()

            self.assertEqual(output, '** class name missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Country')
            output = f.getvalue().strip()

            self.assertEqual(output, '** class doesn\'t exist **')

    def test_create_BaseModel(self):
        '''Test creating a BaseModel instance'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            output_id = f.getvalue().strip()
            objs_dict = self.storage.all()

            self.assertIn(f'BaseModel.{output_id}', objs_dict.keys())

    def test_create_User(self):
        '''Test creating a User instance'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            output_id = f.getvalue().strip()
            objs_dict = self.storage.all()

            self.assertIn(f'User.{output_id}', objs_dict.keys())

    def test_create_State(self):
        '''Test creating a State instance'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State')
            output_id = f.getvalue().strip()
            objs_dict = self.storage.all()

            self.assertIn(f'State.{output_id}', objs_dict.keys())

    def test_create_City(self):
        '''Test creating a City instance'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City')
            output_id = f.getvalue().strip()
            objs_dict = self.storage.all()

            self.assertIn(f'City.{output_id}', objs_dict.keys())

    def test_create_Place(self):
        '''Test creating a Place instance'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place')
            output_id = f.getvalue().strip()
            objs_dict = self.storage.all()

            self.assertIn(f'Place.{output_id}', objs_dict.keys())

    def test_create_Amenity(self):
        '''Test creating a Amenity instance'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Amenity')
            output_id = f.getvalue().strip()
            objs_dict = self.storage.all()

            self.assertIn(f'Amenity.{output_id}', objs_dict.keys())

    def test_create_Review(self):
        '''Test creating a Review instance'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Review')
            output_id = f.getvalue().strip()
            objs_dict = self.storage.all()

            self.assertIn(f'Review.{output_id}', objs_dict.keys())


class TestShowCommand(unittest.TestCase):
    """
    Unittests the `show` command
    """

    def setUp(self):
        '''Runs before every test'''

        self.storage = FileStorage()
        self.storage.reload()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        '''Runs after each test'''

        self.storage._Filestorage__objects = {}

    def test_errors(self):
        '''Test Errors mangement of `show` command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show')
            output = f.getvalue().strip()

            self.assertEqual(output, '** class name missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show Country')
            output = f.getvalue().strip()

            self.assertEqual(output, '** class doesn\'t exist **')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show Review')
            output = f.getvalue().strip()

            self.assertEqual(output, '** instance id missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show City d6586de3-e13b-4553-be56-2ebdb3')
            output = f.getvalue().strip()

            self.assertEqual(output, '** no instance found **')

    def test_show_an_instance(self):
        '''Test showing an instance, ex : BaseModel'''

        base_m = BaseModel()
        base_m.save()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show BaseModel {base_m.id}')
            output = f.getvalue().strip()

            self.assertEqual(output, str(base_m))


class TestDestroyCommand(unittest.TestCase):
    """
    Unittests the `destroy` command
    """

    def setUp(self):
        '''Runs before every test'''

        self.storage = FileStorage()
        self.storage.reload()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        '''Runs after each test'''

        self.storage._Filestorage__objects = {}

    def test_errors(self):
        '''Test Errors mangement of `destroy` command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy')
            output = f.getvalue().strip()

            self.assertEqual(output, '** class name missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy Country')
            output = f.getvalue().strip()

            self.assertEqual(output, '** class doesn\'t exist **')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy Review')
            output = f.getvalue().strip()

            self.assertEqual(output, '** instance id missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy City d6586de3-e13b-4553-be56-2ebdb3')
            output = f.getvalue().strip()

            self.assertEqual(output, '** no instance found **')

    def test_destroy_an_instance(self):
        '''Test destroying an instance, ex : User'''

        user_m = User()
        user_m.save()
        objs_dict = self.storage.all()

        self.assertIn(f'User.{user_m.id}', objs_dict.keys())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'destroy User {user_m.id}')
            output = f.getvalue().strip()

            objs_dict = self.storage.all()

            self.assertNotIn(f'User.{user_m.id}', objs_dict.keys())
