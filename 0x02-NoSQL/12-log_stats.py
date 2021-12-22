#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB

Database: logs
Collection: nginx
Display:
	- First line: x logs where x is the number of documents in the collection
	- second line: "Methods:"
	- 5 lines with the number of documents with the <method> =
	["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
	- one line with the number of documents with:
		- methods=GET
		- path=/status
"""


import pymongo


def log():
    """
    Main function
    """
    client = pymongo.MongoClient()
    db = client.logs
    collection = db.nginx

    print("{} logs".format(collection.count_documents({})))

    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    for method in methods:
        print("\tmethod {}: {}".format(
            method, collection.count_documents({"method": method})))

    print("{} status check".format(collection.count_documents(
        {"method": "GET", "path": "/status"})))


if __name__ == "__main__":
    log()
