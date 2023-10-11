#!/usr/bin/python3
'''This module implements the BaseModel class'''
import models
import datetime
import uuid


class User(models.base_model.BaseModel):
    '''
    The User class that inherits from BaseModel

    Public class attributes:
        email (string) : empty string
        password (string) : empty string
        first_name (string) : empty string
        last_name (string) : empty string
    '''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
