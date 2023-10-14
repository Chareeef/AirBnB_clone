#!/usr/bin/python3
"""This module implements the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    The City class that inherits from BaseModel

        Public class attributes:
                state_id: string - empty string: it will be the State.id
                name: string - empty string
    """

    state_id = ""
    name = ""
