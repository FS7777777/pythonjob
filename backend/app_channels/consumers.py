from django.http import HttpResponse
from channels.handler import AsgiHandler

def http_consumer(message):
    response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)

def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    message.reply_channel.send({
        "text": message.content['text'],
    })