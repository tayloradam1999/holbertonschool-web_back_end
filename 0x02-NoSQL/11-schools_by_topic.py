#!/usr/bin/env python3
"""
Returns the list of schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
	"""
	Args:
		mongo_collection: A pymongo.collection object
		topic: The topic to search for
	
	Returns:
		- A list of schools having the topic
		- Empty list if no schools
	"""
	return mongo_collection.find({'topics': topic})
