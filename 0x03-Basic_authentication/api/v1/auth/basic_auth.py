#!/usr/bin/env python3
"""
Manage 'Basic' type authentication
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Manage 'Basic' AUTH_TYPE
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Returns Base64 part of <Authorization> header for Basic Authentication.

        Args:
            authorization_header (str): The value of the header key

        Returns:
            None if <authorization_header> is None
            None if <authorization_header> is not a str
            None if authorization_header doesn't start with 'Basic'
                Otherwise, return the value after 'Basic'
            
        You can assume <authorization_header> contains only one 'Basic'
        """
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]
