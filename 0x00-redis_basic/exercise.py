#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """
    Stores the history of inputs and outputs for a particular function in
    the Cache() class.

    Everytime a method is called, adds input parameters to one list in redis,
    and its output into another redis list.

    Uses __qualname__ dundermethod to append ":inputs" and ":outputs" to create
    input and output list keys.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Uses rpush to append input arguments.

        Use str(args) to normalize.

        Ignore potential kwargs.
        """
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(f"{key}:outputs", str(output))
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    Counts the number of times a Cache() method is called.

    As a key, uses the qualified name of <method> using the
    __qualname__ dunder method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """
    Stores an instance of the Redis client as a private variable
    named <_redis> (using redis.Redis()) and flushes the instance
    using the flushdb() method.
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
        self._redis.set(key, data)
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


def replay(method: Callable) -> Callable:
    """
    Displays the history of calls of a particular method.

    Uses keys previously generated to generate required output.

    Uses lrange and zip to loop over inputs and outputs.
    """
    instance = redis.Redis()
    qn = method.__qualname__
    cache = Cache()
    inputs = instance.lrange(f"{qn}:inputs", 0, -1)
    outputs = instance.lrange(f"{qn}:outputs", 0, -1)
    print("{} was called {} times:".format(qn, instance.get(qn)))
    for input, output in zip(inputs, outputs):
        print(f"{qn}(*{input.decode('UTF-8')}) -> {output}")
