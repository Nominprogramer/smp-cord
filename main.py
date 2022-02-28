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
    pass

def StopServer():
    pass


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    # noinspection PyMethodMayBeStatic
    async def on_message(self, message):
        if message.content.startswith("$", 0):
            if message.content == "$start":
                await message.channel.send("Attempting to start server")
                if ServerStatus():
                    await message.channel.send("Server is already online :D")
                else:
                    StartServer()

            elif message.content == "$stop":
                await message.channel.send("Attempting to stop server")
                if not ServerStatus():
                    await message.channel.send("Server is already Offline")
                else:
                    StopServer()


client = MyClient()
client.run('OTQwMTAzOTkzMzQwODY2NjUx.YgCiEg._H0L3cFSYsmDhax4uXndcYSDLWg')
