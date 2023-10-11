#!/usr/bin/python3
'''This module implements the FileStorage class'''
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

        return FileStorage.__objects

    def new(self, obj):
        '''Sets in __objects the obj with key <obj class name>.id'''

        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        '''Serializes __objects to the JSON file (path: __file_path)'''

        dict_objs = {}
        for key, obj in FileStorage.__objects.items():
            dict_objs[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(dict_objs, f)

    def reload(self):
        '''Deserializes the JSON file to __objects'''

        try:
            with open(FileStorage.__file_path, encoding='utf-8') as f:
                dict_objs = json.load(f)

            from models.base_model import BaseModel
            from models.user import User

            classes = {
                    'BaseModel': BaseModel,
                    'User': User
                    }

            for key, obj_dict in dict_objs.items():
                cls_name, inst_id = key.split('.')
                cls = classes[cls_name]
                new_obj = cls(**obj_dict)
                self.new(new_obj)

        except FileNotFoundError:
            return
