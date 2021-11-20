#!/usr/bin/env python3
"""
Manage API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """
    Manage Api Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method that returns True if the <path> is not in the list of strings
        <excluded_paths>.

        You can assume <excluded_paths> contains string path always ending
        with a '/'.

        This method is slash intolerant. For example, if <path> is '/v1/auth'
        and <excluded_paths> is ['/v1/auth/', '/v1/auths/'], then this method
        will return False.

        Additional Returns:
            True if <path> is None
            True if <excluded_paths> is None or empty
            False if <path> is in <excluded_paths>
        """
        if excluded_paths is None or len(excluded_paths) == 0 or path is None:
            return True
        path = str(path)
        if path in excluded_paths or path + '/' in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        HTTP header authorization

        Returns:
            If <request> is None, returns None.
            If <request> doesn't contain the header key <'Authorization'>,
            returns None.
            Otherwise, returns the value of the header key <'Authorization'>.
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns:
            None

        <request> will be the Flask request object.
        """
        return None
