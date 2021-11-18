#!/usr/bin/env python3
"""
Use <bcrypt> to perform hasing on password
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns salted, hashed byte string password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
