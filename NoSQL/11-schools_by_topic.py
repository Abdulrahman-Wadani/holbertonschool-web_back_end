#!/usr/bin/env python3
"""
Module that lists all documents in a MongoDB collection
"""


def schools_by_topic(mongo_collection, topic):
    """
    Lists all documents in a collection.
    Returns an empty list if no document in the collection.
    """
    return list(mongo_collection.find({'topics': topic}))
