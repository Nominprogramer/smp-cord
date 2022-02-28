import discord
import minestat

def ServerStatus() -> object:
    ms = minestat.MineStat("64.227.162.110", 25565)
    # print(ms.online)
    if ms.online == True:
        return True
    else:
        return False


def StartServer():
    if start_msg.find(start_passwd) != -1:
                   print(str(message.author) + "has passed auth , Starting Server!")
def StopServer():
    if message.content.startswith('$stop'):
            if stop_msg.find(stop_passwd) != -1:
                   print(str(message.author) + "has passed auth , Starting Server!")

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
                await message.channel.send("Attempting to start server")
                if ServerStatus():
                    await message.channel.send("Server is already online :D")
                else:
                    StartServer()

        elif message.content == "$stop":
             stop_msg = message.content
             await message.channel.send("Attempting to stop server")
             if not ServerStatus():
                 await message.channel.send("Server is already Offline")
             else:
                 StopServer()


client = MyClient()
client.run('OTQwMTAzOTkzMzQwODY2NjUx.YgCiEg._H0L3cFSYsmDhax4uXndcYSDLWg')
