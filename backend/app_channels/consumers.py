from channels import Group

# Connected to websocket.connect
def ws_add(message,room_name):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    #Group("chat").add(message.reply_channel)
    Group("chat-%s" % room_name).add(message.reply_channel)

# Connected to websocket.receive
def ws_message(message, room_name):
    Group("chat-%s" % room_name).send({
        "text": "[user] %s" % message.content['text'],
    })

# Connected to websocket.disconnect
def ws_disconnect(message, room_name):
    Group("chat-%s" % room_name).discard(message.reply_channel)