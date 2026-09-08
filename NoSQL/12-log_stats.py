#!/usr/bin/env python3
"""
Module that lists all documents in a MongoDB collection
"""
if __name__ == "__main__":
    from pymongo import MongoClient

    clint = MongoClient('mongodb://127.0.0.1:27017')
    nginc_collection = clint.logs.nginx

    print(f'{nginc_collection.count_documents({})} logs')
    print(f"Methods:\
        \n\tmethod GET: {nginc_collection.count_documents({'method': 'GET'})}\
        \n\tmethod POST: {nginc_collection.count_documents(
        {'method': 'POST'})}\
        \n\tmethod PUT: {nginc_collection.count_documents({'method': 'PUT'})}\
        \n\tmethod PATCH: {nginc_collection.count_documents(
            {'method': 'PATCH'})}\
        \n\tmethod DELETE: {nginc_collection.count_documents(
                {'method': 'DELETE'})}"
    )
    print(f"{nginc_collection.count_documents(
        {'method': 'GET', 'path': '/status'})} status check")
