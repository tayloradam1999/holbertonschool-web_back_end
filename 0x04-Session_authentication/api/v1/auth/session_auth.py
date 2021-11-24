#!/usr/bin/env python3
"""
Session Authentication Module
"""
from api.v1.auth.auth import Auth
import uuid
from os import getenv


SESSION_NAME = getenv("SESSION_NAME")


class SessionAuth(Auth):
    """
    Handles Session Authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a <user_id>

        Args:
            user_id (str): The user's ID

        Returns:
            None if <user_id> is None
            None if <user_id> is not a string
            Otherwise:
                Generates a session ID using the `uuid` module and
                    uuid4() like <id> in <Base>
                Uses new session ID as key of the dict <user_id_by_session_id>,
                    the value for this key must be <user_id>
                Returns the session ID

        The same <user_id> can have multiple session IDs. The <user_id> is
            the value in the dictionary <user_id_by_session_id>
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        # assigns session_id to key, user_id to value
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns the user ID for a <session_id>

        Uses .get() to get the value for the key <session_id> in
        <user_id_by_session_id>

        Args:
            session_id (str): The session ID

        Returns:
            None if <session_id> is None
            None if <session_id> is not a string
            The value (The user ID) for the key <session_id> in
                <user_id_by_session_id>
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        my_session_id = self.user_id_by_session_id.get(session_id)
        return my_session_id

    def session_cookie(self, request=None):
        """
        Returns a cookie value from a request

        Uses .get_cookies() to get the cookies from <request>

        Uses env variable <SESSION_NAME> to define the name of the cookie
            used for the session ID

        Args:
            request (obj): The request object

        Returns:
           None if <request> is None
           The value of the cookie named <_my_session_id> from <request> -
                the name of the cookie must be defined by the env variable
                    <SESSION_NAME>
        """
        if request is None:
            return None
        my_cookies = request.get_cookies()
        if '_my_session_id' in my_cookies:
            return my_cookies['_my_session_id']
