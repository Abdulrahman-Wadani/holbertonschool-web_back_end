#!/usr/bin/env python3
""" Module for task 12: Provides some stats about Nginx logs """

from pymongo import MongoClient


def log_stats():
    """ Print stats about Nginx logs """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    get_status = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{get_status} status check")


if __name__ == "__main__":
    log_stats()
