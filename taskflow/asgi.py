import os

from channels.routing import ProtocolTypeRouter

from channels.routing import URLRouter

from channels.auth import AuthMiddlewareStack

from django.core.asgi import get_asgi_application

import productivity.routing


os.environ.setdefault(

'django.settings.module',

'taskflow.settings'
)


application = ProtocolTypeRouter({

"http":

get_asgi_application(),

"websocket":

AuthMiddlewareStack(

URLRouter(

productivity.routing.websocket_urlpatterns
)
),
})