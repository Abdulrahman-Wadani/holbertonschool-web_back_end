#!/usr/bin/env python3
"""
Module that lists all documents in a MongoDB collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Lists all documents in a collection.
    Returns an empty list if no document in the collection.
    """
    return mongo_collection.insert(kwargs)
