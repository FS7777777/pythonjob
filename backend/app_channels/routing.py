from channels.routing import route
from app_channels.consumers import ws_message

channel_routing = [
    route("http.request", "app_channels.consumers.http_consumer"),
    #route("websocket.receive", ws_message),
]