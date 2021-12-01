#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from typing import TypeVar

from user import Base
from user import User


class DB:
    """
    DB class
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Returns a User object and saves it to the database
        """
        my_user = User(email=email, hashed_password=hashed_password)
        self._session.add(my_user)
        self._session.commit()
        return my_user

    def find_user_by(self, **kwargs) -> TypeVar('User'):
        """
        Returns a User object if found in database

        NoResultFound and InvalidRequestError are raised when no results
        are found, or when wrong query arguments are passed, respectively.
        """
        try:
            return self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound
        except InvalidRequestError:
            raise InvalidRequestError

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Uses find_user_by to locate user and then updates it

        If an arg doesn't correspond to the user, raise ValueError
        """
        my_user = self.find_user_by(id=user_id)
        for arg in kwargs:
            try:
                setattr(my_user, arg, kwargs[arg])
            except:
                raise ValueError

        self._session.commit()
