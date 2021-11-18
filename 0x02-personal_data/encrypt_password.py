#!/usr/bin/env python3
"""
Use <bcrypt> to perform hasing on password

Use <bcrypt> to validate password
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns salted, hashed byte string password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates password
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
