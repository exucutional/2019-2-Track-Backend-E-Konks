from channels.routing import ProtocolTypeRouter, URLRouter
import messages.routing

application = ProtocolTypeRouter({
    'http': URLRouter(messages.routing.urlpatterns),
})