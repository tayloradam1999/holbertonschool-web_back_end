#!/usr/bin/env python3
"""
Hashes password
"""
import bcrypt
from typing import TypeVar
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Returns salted and hashed password using bcrypt.hashpw()
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """
    Auth class to interact with the authentication database
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> TypeVar('User'):
        """
        Hashes password with _hash_password, then saves user to database
        using self._db.add_user() and then returns the User object


        If a used already exists with the passed email, raise ValueError
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists.".format(email))
        except NoResultFound:
            my_user = self._db.add_user(email, _hash_password(password))
            return my_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Returns True if user exists and password is correct
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False
