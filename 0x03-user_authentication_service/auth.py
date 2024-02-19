#!/usr/bin/env python3
""" Authentication Module
"""
from db import DB
from user import User

from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NoResultFound
from typing import Union
from uuid import uuid4


def _hash_password(password: str) -> str:
    """ This method takes in string arg, converts to unicode
    Returns salted, hashed pswd as bytestring
    """
    return hashpw(password.encode('utf-8'), gensalt())


def _generate_uuid() -> str:
    """ This method generates UUID
    returns string representation of new UUID
    """
    return str(uuid4())


class Auth:
    """The Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Initializes an Instance """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ This method registers and returns a new user if
            email isn't listed
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """ This method checks if user pswd is valid, locating by email """
        try:
            found_user = self._db.find_user_by(email=email)
            return checkpw(
                password.encode('utf-8'),
                found_user.hashed_password
                )
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ This method creates session ID using UUID, finds user by email """
        try:
            found_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(found_user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """ This method finds user by session_id """
        if session_id is None:
            return None
        try:
            found_user = self._db.find_user_by(session_id=session_id)
            return found_user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: str) -> None:
        """ This method updates user's session_id to None """
        if user_id is None:
            return None
        try:
            found_user = self._db.find_user_by(id=user_id)
            self._db.update_user(found_user.id, session_id=None)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ This method finds user by email, updates user's reset_token
        with UUID
        """
        try:
            found_user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        reset_token = _generate_uuid()
        self._db.update_user(found_user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """ This method finds user by reset_token, updates user's pswd """
        try:
            found_user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        new_pswd = _hash_password(password)
        self._db.update_user(
            found_user.id,
            hashed_password=new_pswd,
            reset_token=None)
