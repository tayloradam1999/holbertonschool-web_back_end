#!/usr/bin/env python3
"""
Manage 'Basic' type authentication
"""
from api.v1.auth.auth import Auth
import base64


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
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """
        Returns the decoded value of the Base64 string
        <base64_authorization_header>

        Args:
            base64_authorization_header: The Base64 string

        Returns:
            None if <base64_authorization_header> is None
            None if <base64_authorization_header> is not a string
            None if <base64_authorization_header> is not valid Base64
                (Use try/except)
            Otherwise, return decoded value as UTF8 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(
                            base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> str:
        """
        Returns the user email and password from the Base64 decoded value in
        a tuple.

        Args:
            decoded_base64_authorization_header: The Base64 decoded value

        Returns:
            (None, None) if <decoded_base64_authorization_header> is None
            (None, None) if <decoded_base64_authorization_header> is not a str
            (None, None) if <decoded_base64_authorization_header> doesn't
                contain ':' (Use try/except)
            Otherwise, return the user email and password. These 2 values
            must be seperated by a ':'

        You can assume <decoded_base64_authorization_header> will contain
        only one ':'
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        try:
            a, *b = decoded_base64_authorization_header.split(":")
            return (a, b[0])
        except Exception:
            return (None, None)
