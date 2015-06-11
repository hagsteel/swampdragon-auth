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


## Token authentication (thanks to @silentninja)

1.  Add the following to the settings file:

`SWAMP_DRAGON_CONNECTION = ('swampdragon.socketconnection.RemoteDataConnection', '/data')`

2.  Add the TokenAuthMixin to your router:

```
from swampdragon_tokenauth.mixins import TokenAuthMixin
from swampdragon.route_handler import ModelRouter
```

### TokenAuthMixin should come before the model router

    class TodoItemRouter(TokenAuthMixin,ModelRouter):
        route_name = 'todo-item'
        serializer_class = TodoItemSerializer
        model = TodoItem
        permission_classes = [LoginRequired()]
    
        def get_object(self, **kwargs):
            return self.model.objects.get(pk=kwargs['id'])
    
        def get_query_set(self, **kwargs):
            return self.model.objects.filter(todo_list__id=kwargs['list_id'])    


Pass in the drf auth token as 'auth' argument when subscribing to a channel:

In angularjs:

    $dragon.onReady(function() {
        $dragon.subscribe('todo-item', $scope.channel, {auth:"your_auth_token"}).then(function(response) {
            // code
        });
        })


## Contributing

Contributions are more than welcome, just make sure your pull request works with both python 2.7 and 3.4
