import discord

start_paswd = "sudoStartServer"
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
               if start_msg.find(start_paswd) != -1:
                   print(message.author)



client.run('OTQwMTAzOTkzMzQwODY2NjUx.YgCiEg._H0L3cFSYsmDhax4uXndcYSDLWg')

