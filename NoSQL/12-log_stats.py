#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""
if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # 1. طباعة إجمالي السجلات
    print(f"{nginx_collection.count_documents({})} logs")

    # 2. طباعة الإحصائيات للطرق (Methods)
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")

    # 3. طباعة فحص الحالة (Status check)
    status_count = nginx_collection.count_documents(
        {'method': 'GET', 'path': '/status'}
    )
    print(f"{status_count} status check")
