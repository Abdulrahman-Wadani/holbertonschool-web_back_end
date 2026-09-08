#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_logs = nginx_collection.count()
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count({'method': method})
        print(f"\tmethod {method}: {count}")

    status_count = nginx_collection.count({'method': 'GET', 'path': '/status'})
    print(f"{status_count} status check")
