from django.conf import settings
from django.contrib.auth import login, get_user_model
from django.contrib.sessions.models import Session
from swampdragon.connections.sockjs_connection import DjangoSubscriberConnection
from session_decoder import decode_session


class HttpDataConnection(DjangoSubscriberConnection):
    def __init__(self, session):
        self._user = None
        super(HttpDataConnection, self).__init__(session)

    def get_user(self):
        try:
            if self._user is not None:
                return self._user
            cookie_name = getattr(settings, 'SESSION_COOKIE_NAME', 'sessionid')
            morsel = self.session.conn_info.cookies.get(cookie_name)
            session = Session.objects.get(session_key=morsel.value)
            decoded_session = decode_session(session)
            self._user = get_user_model().objects.get(pk=decoded_session['_auth_user_id'])
        except:
            self._user = None
        return self._user

    @property
    def user(self):
        return self.get_user()
