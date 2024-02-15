#!/usr/bin/env python3
"""
API session authentication module
"""

from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ Session Authentication """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ This method creates a Session ID for user_id """

        if user_id is None or isinstance(user_id, str) is False:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ This method returns User ID based on Session ID """

        if session_id is None or isinstance(session_id, str) is False:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ This method returns a User instance based on cookie value """

        session_id = self.session_cookie(request)

        return User.get(self.user_id_for_session_id(session_id))

    def destroy_session(self, request=None):
        """ This method deletes user session to logout """

        if self.session_cookie(request) is None:
            return False

        session_id = self.session_cookie(request)

        if self.user_id_for_session_id(session_id) is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True
