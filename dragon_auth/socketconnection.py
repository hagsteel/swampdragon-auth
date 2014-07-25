from django.contrib.auth import login, get_user_model
from django.contrib.sessions.models import Session
from swampdragon.connections.sockjs_connection import DjangoSubscriberConnection


class HttpDataConnection(DjangoSubscriberConnection):
    def __init__(self, session):
        self._user = None
        super(HttpDataConnection, self).__init__(session)

    def get_user(self):
        try:
            if self._user is not None:
                return self._user
            morsel = self.session.conn_info.cookies.get('sessionid')
            session = Session.objects.get(session_key=morsel.value)
            decoded_session = session.get_decoded()
            self._user = get_user_model().objects.get(pk=decoded_session['_auth_user_id'])
        except:
            self._user = None
        return self._user

    @property
    def user(self):
        return self.get_user()
