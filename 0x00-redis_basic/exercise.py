#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union


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

        Returns the key.
        """
        key = str(uuid.uuid4())
        Cache()._redis.set(key, data)
        return key
