
class TokenAuthMixin(object):
    def handle(self,data):
        if data['verb'] == 'subscribe' and 'auth' in data['args']:
            auth_token = data['args'].pop('auth')
            self.connection.authenticate(auth_token)
        super(TokenAuthMixin, self).handle(data)
