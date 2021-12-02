#!/usr/bin/env python3
"""
Module used to authenticate users to database.
"""
import bcrypt
import uuid
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """
    Returns salted and hashed password using bcrypt.hashpw()
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Returns string representation of a new UUID
    """
    return str(uuid.uuid4())


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
            return self._db.add_user(email, _hash_password(password))

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
                return bcrypt.checkpw(password.encode('utf-8'),
                                      user.hashed_password)
            return False
        except NoResultFound as e:
            return False

    def create_session(self, email: str) -> str:
        """
        Finds user corresponding to email, generates new UUID,
        saves UUID to database as the user's session_id,
        then return the session_id

        Args:
            email (str): user's email

        Returns:
            str: UUID
        """
        user = self._db.find_user_by(email=email)
        session_id = _generate_uuid()
        user.session_id = session_id
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Returns corresponding User object from session_id

        Args:
            session_id (str): UUID

        Returns:
            If session ID is None, or no user found, return None
            Otherwise, return User object
        """
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound as e:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Updates corresponding user's session_id to None

        Args:
            user_id (int): user's id

        Returns:
            None
        """
        user = self._db.find_user_by(id=user_id)
        user.session_id = None

    def get_reset_password_token(self, email: str) -> str:
        """
        Finds corresponding user to email. Generates UUID
        and updates the user's <reset_token> database field.
        Then returns the reset_token

        Args:
            email (str): user's email

        Returns:
            If user does not exist, raises ValueError
            Otherwise, returns reset_token
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                reset_token = _generate_uuid()
                self._db.update_user(user.id, reset_token=reset_token)
                return reset_token
        except Exception as e:
            raise ValueError()
