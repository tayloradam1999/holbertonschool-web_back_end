#!/usr/bin/env python3
"""
Changes all topics of a school document based on the name of the school
"""


def update_topics(mongo_collection, name, topics):
	"""
	Args:
		mongo_collection: A pymongo.collection object
		name: The name of the school to update
		topics: A list of topics to update
	
	Returns:
		- The document updated
		- None if no document updated
	"""
	return mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
