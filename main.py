import discord

start_passwd = ""
stop_passwd = ""
client = discord.Client()

@client.event
async def on_ready():
        print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
        if message.author == client.user:
                return

        if message.content.startswith('$hello'):
                await message.channel.send('Hello!')

        if message.content.startswith('$start'):
               start_msg = message.content
               if start_msg.find(start_passwd) != -1:
                   print(str(message.author) + "has passed auth , Starting Server!")
        if message.content.startswith('$stop'):
                     start_msg = message.content
                     if start_msg.find(stop_passwd) != -1:
                                 print(str(message.author) + "has passed auth , Starting Server!")



client.run('OTQwMTAzOTkzMzQwODY2NjUx.YgCiEg._H0L3cFSYsmDhax4uXndcYSDLWg')

