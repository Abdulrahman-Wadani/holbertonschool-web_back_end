#!/usr/bin/env python3
"""
Module that lists all documents in a MongoDB collection
"""
import pymongo


def update_topics(mongo_collection: pymongo, name, topics):
    """
    Lists all documents in a collection.
    Returns an empty list if no document in the collection.
    """
    return mongo_collection.UpdateMany(name, topics)
