#!/usr/bin/env python
"""
Create a class BasicCache that inherits from BaseCaching
and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    -You must use self.cache_data: dictionary from the parent class BaseCaching
    -This caching system doesn’t have limit
    """

    def put(self, key, item):
        """
        -Assigns to the dict <self.cache_data> the item value for the key
        -If key or item is None, this method should not do anything.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        -Returns the value in self.cache_data linked to key.
        -If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
