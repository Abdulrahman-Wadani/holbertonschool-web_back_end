#!/usr/bin/env python3
"""
Module that lists all documents in a MongoDB collection
"""


def update_topics(mongo_collection, name, topics):
    """
    Lists all documents in a collection.
    Returns an empty list if no document in the collection.
    """
    return mongo_collection.update_many(
        {'name': name}, {'$set': {'topics': topics}})
