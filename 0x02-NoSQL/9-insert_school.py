#!/usr/bin/env python3
"""
Inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
	"""
	Args:
		mongo_collection: A pymongo.collection object
		kwargs: A dictionary of key-value pairs to insert in the collection
	
	Returns:
		- The document inserted
		- None if no document inserted
	"""
	return mongo_collection.insert_one(kwargs).inserted_id
