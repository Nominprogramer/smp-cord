import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    # noinspection PyMethodMayBeStatic
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.startswith("$", 0):
            print("Command")

            if message.content == "$start":
                print("Attempting to start server")

            elif message.content == "$stop":
                print("Attempting to stop server")


client = MyClient()
client.run('OTQwMTAzOTkzMzQwODY2NjUx.YgCiEg._H0L3cFSYsmDhax4uXndcYSDLWg')
