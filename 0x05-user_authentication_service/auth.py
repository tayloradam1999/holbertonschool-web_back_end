#!/usr/bin/env python3
"""
Module used to authenticate users to database.
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


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

    def register_user(self, email: str, password: str) -> User:
        """
        Hashes password with _hash_password, then saves user to database
        using self._db.add_user() and then returns the User object


        If a user already exists with the passed email, raise ValueError

        Args:
            email (str): user's email
            password (str): user's password

        Returns:
            User: User object
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound as e:
            return self._db.add_user(email, self._hash_password(password))
                

    def valid_login(self, email: str, password: str) -> bool:
        """
        Returns True if user exists and password is correct

        Args:
            email (str): user's email
            password (str): user's password

        Returns:
            bool: True if user exists and password is correct
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(password.encode('utf-8'), user.password)
            return False
        except NoResultFound as e:
            return False
