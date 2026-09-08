#!/usr/bin/env python3
"""
Module that lists all documents in a MongoDB collection
"""
if __name__ == "__main__":
    from pymongo import MongoClient

    clint = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = clint.logs.nginx

    print(f'{nginx_collection.count_documents({})} logs')
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")
    print(f"{nginx_collection.count_documents({'method': 'GET',
                                               'path': '/status'})} status check")
