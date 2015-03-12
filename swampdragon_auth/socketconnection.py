from importlib import import_module
from django.conf import settings
from django.contrib.auth import get_user
from swampdragon.connections.sockjs_connection import DjangoSubscriberConnection


class _RequestWrapper(object):

    def __init__(self, session):
        self.session = session


class HttpDataConnection(DjangoSubscriberConnection):

    def __init__(self, session):
        self._user = None

        engine = import_module(settings.SESSION_ENGINE)
        self.SessionStore = engine.SessionStore
        super(HttpDataConnection, self).__init__(session)

    def get_user(self):
        if self._user is not None:
            return self._user

        cookie_name = settings.SESSION_COOKIE_NAME
        morsel = self.session.conn_info.cookies.get(cookie_name)
        if morsel is not None:
            session = self.SessionStore(morsel.value)
            user = get_user(_RequestWrapper(session))
            if user and not user.is_anonymous():
                self._user = user

        return self._user

    @property
    def user(self):
        return self.get_user()


class RemoteDataConnection(DjangoSubscriberConnection):

    def __init__(self, session):
        self._user = None
        try:
            from rest_framework.authtoken.models import Token
        except ImportError:
            raise ImportError(
                "Django Rest Framework is required")
        super(RemoteDataConnection, self).__init__(session)

    def get_user(self):
        return self._user

    @property
    def user(self):
        return self.get_user()

    def authenticate(self, token):
        try:
            t = Token.objects.get(key=token)
            self._user = t.user
        except Token.DoesNotExist:
            self._user = None
