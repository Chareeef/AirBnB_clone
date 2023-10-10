#!/usr/bin/python3
'''This module implements the FileStorage class'''
from models.base_model import BaseModel
import json


class FileStorage():
    '''
    A FileStorage class that serializes instances to a JSON file
    and deserializes JSON file to instances

    Private class attributes:
        __file_path (str) - path to the JSON file (ex: file.json)
        __objects (dict) - empty but will store all objects by <class name>.id

    Public instance methods:
        all(self):
        new(self, obj)
        save(self)
        reload(self)
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects'''

        return self.__objects

    def new(self, obj):
        '''Sets in __objects the obj with key <obj class name>.id'''

        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        '''Serializes __objects to the JSON file (path: __file_path)'''

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            for obj in self.__objects.values():
                json.dump(obj.to_dict(), f)

    def reload(self):
        '''Deserializes the JSON file to __objects'''

        try:
            with open(self.__file_path, encoding='utf-8') as f:
                json_strings = f.readlines()

                for json_str in json_strings:
                    obj_dict = json.loads(json_str)
                    obj = BaseModel(**obj_dict)
                    self.new(obj)

        except FileNotFoundError:
            return
