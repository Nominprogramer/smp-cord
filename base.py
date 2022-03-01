import discord

cmd_alias = $

@client.event
async def on_ready():
    print("logged in as {0.user}".format(client)) #notifies when bot logs in

@client.event
async def on_message(message):
    sender = str(message.author)
    content = (message.content)

    if sender == client.user: #Ignores messages by the bot
        return
    if content.startswith(cmd_alias) #checks only command messages and not user messages
        command_recived = true
    else command_recived = false #Ignore messages that are not commands
        return
    if content == cmd_alias+"start"
        print("Starting Server on the request of " + sender)
    if content == cmd_alias+"stop"
        print("Stopping Server on the request of " + sender)

