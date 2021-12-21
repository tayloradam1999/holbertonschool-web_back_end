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
import sys
import os


def main():
	"""
	Main function
	"""
	if len(sys.argv) != 2:
		print("Usage: {} <db_name>".format(os.path.basename(sys.argv[0])))
		sys.exit(1)
	db_name = sys.argv[1]
	client = pymongo.MongoClient()
	db = client[db_name]
	collection = db['nginx']
	print("{} logs where {} is the number of documents in the collection".format(
		collection.count(), collection.count()))
	print("Methods:")
	methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
	for method in methods:
		print("{} = {}".format(method, collection.count({'method': method})))
	print("Methods=GET")
	print("Path=/status = {}".format(collection.count({'method': 'GET', 'path': '/status'})))
