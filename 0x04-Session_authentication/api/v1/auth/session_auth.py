#!/usr/bin/env python3
"""
Session Authentication Module
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    Handles Session Authentication
    """
    def __init__(self):
        """
        Init method
        """
        self.user_id_by_session_id = {}

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
        self.user_id_by_session_id[session_id] = user_id
        return session_id
