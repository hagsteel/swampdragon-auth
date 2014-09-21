Swamp Dragon auth
=================

# Installation
```pip install swampdragon-auth```


# Django settings.py file
Add the following code to your settings file:

    SWAMP_DRAGON_CONNECTION = ('swampdragon_auth.socketconnection.HttpDataConnection', '/data')


## Important note about deployment

If you are running your SwampDragon instances on a subdomain, you need to set 

    SESSION_COOKIE_DOMAIN = .yourdomain.tld
    
or the authentication won't be able to access the user.

To access a signed in user in your router:

    self.connection.get_user()
    
or

    self.connection.user
