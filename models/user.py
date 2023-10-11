#!/usr/bin/python3
"""Module to create a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Subclass for user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
