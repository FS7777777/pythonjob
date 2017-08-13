from channels.routing import route
from app_channels.consumers import ws_add,ws_message,ws_disconnect

channel_routing = [
    route("websocket.connect", ws_add,path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
    route("websocket.receive", ws_message,path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
    route("websocket.disconnect", ws_disconnect,path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
]