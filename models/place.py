#!/usr/bin/python3
"""Module that creates a Place subclass"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Subclass for User place objects
        city_id:             (string)
        user_id:             (string)
        name:                (string)
        description:         (string)
        number_rooms:        (int) 0
        number_bathrooms:    (int) 0
        max_guest:           (int) 0
        price_by_night:      (int) 0
        latitude:            (float) 0.0
        longitude:           (float) 0.0
        amenity_ids:         (list)
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
