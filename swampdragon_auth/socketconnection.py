from importlib import import_module
from django.conf import settings
from django.utils.module_loading import import_string
from swampdragon.connections.sockjs_connection import DjangoSubscriberConnection

SESSION_KEY = '_auth_user_id'
BACKEND_SESSION_KEY = '_auth_user_backend'
HASH_SESSION_KEY = '_auth_user_hash'


def load_backend(path):
    backend = import_string(path)()
    if backend:
        return backend
    return None


class HttpDataConnection(DjangoSubscriberConnection):
    def __init__(self, session):
        self._user = None

        engine = import_module(settings.SESSION_ENGINE)
        self.SessionStore = engine.SessionStore
        super(HttpDataConnection, self).__init__(session)

    def get_user(self):
        if self._user is not None:
            return self._user

        try:
            cookie_name = getattr(settings, 'SESSION_COOKIE_NAME', 'sessionid')
            morsel = self.session.conn_info.cookies.get(cookie_name)
            session = self.SessionStore(morsel.value)

            backend = load_backend(session.get(BACKEND_SESSION_KEY))

            if not backend:
                return None

            self._user = backend.get_user(session.get(SESSION_KEY))
        except:
            self._user = None
        return self._user

    @property
    def user(self):
        return self.get_user()
