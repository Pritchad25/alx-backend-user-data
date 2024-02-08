#!/usr/bin/env python3
""" The Module for Encrypting pswds with bcrypt """

import bcrypt


def hash_password(password: str) -> bytes:
    """ This method takes in string arg, converts to unicode
    Returns salted, hashed pswd as bytestring
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ This method checks if hashed and unhashed pswds are same
    Returns bool
    """
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False
