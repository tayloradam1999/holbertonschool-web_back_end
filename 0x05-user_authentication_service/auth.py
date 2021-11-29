#!/usr/bin/env python3
"""
Hashes password
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Returns salted and hashed password using bcrypt.hashpw()
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
