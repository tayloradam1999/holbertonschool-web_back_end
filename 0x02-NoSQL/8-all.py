#!/usr/bin/env python3
"""
Lists all documents in a mongodb collection
"""


def list_all(mongo_collection):
	"""
	Args:
		mongo_collection: A pymongo.collection object
	
	Returns:
		- All documents in collection
		- Empty list if no documents
	"""
	return mongo_collection.find()
