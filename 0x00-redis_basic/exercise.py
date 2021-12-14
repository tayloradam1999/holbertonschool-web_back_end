#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union, Callable


class Cache():
    """
    Stores an instance of the Redis client as a private variable
    named <_redis> (using redis.Redis()) and flushes the instance
    using the flushdb() method.
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates random key with uuid and stores the input
        data in Redis using the key.

        Args:
            data (Union[str, bytes, int, float]): data to be stored

        Returns:
            str: key of the stored data
        """
        key = str(uuid.uuid4())
        Cache()._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable[[bytes], str] = None) -> str:
        """
        Takes key argument and returns the corresponding data
        from Redis using the get() method. If the data is not
        found in Redis, it calls the function fn and stores the
        returned data in Redis using the key.

        Args:
            key (str): key of the data to be retrieved
            fn (Callable[[bytes], str]): function to be called
                if the data is not found in Redis

        Returns:
            str: data stored in Redis
        """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """
        Automatically parameterizes <Cache.get> with the correct
        conversion function

        Args:
            key (str): key of the data to be retrieved

        Returns:
            str: data stored in Redis
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """
        Automatically parameterizes <Cache.get> with the correct
        conversion function

        Args:
            key (str): key of the data to be retrieved

        Returns:
            int: data stored in Redis
        """
        return self.get(key, int)
