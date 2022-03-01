import discord
import minestat
import os.path


def ServerStatus() -> object:
    ms = minestat.MineStat("64.227.162.110", 25565)
    # print(ms.online)
    # noinspection PySimplifyBooleanCheck
    if ms.online == True:
        return True
    else:
        return False


def log(file, msg):
    if os.path.exists(file):
        logfile = open(file, "a")
    else:
        # noinspection PyUnusedLocal
        logfile = open(file, "x")
        logfile = open(file, "a")

    logfile.write(msg)
    logfile.close()  # good practice


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    sender = str(message.author)
    # logger.debug(sender)
    # logger.debug(message.content)
    # log('discord.log', sender)
    # log('discord.log', message.content)

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$start'):
        await message.channel.send("Attempting to start server")
        if ServerStatus():
            await message.channel.send("Server is already online :D")
        else:
            await message.channel.send("Starting Server on the request of" + sender + '\n')
            print("Starting Server on the request of" + sender)
            log("discord.log", sender + ', ')

    elif message.content == "$stop":
        sender = message.author
        await message.channel.send("Attempting to stop server")
        if not ServerStatus():
            await message.channel.send("Server is already Offline")
        else:
            print("Stopping Server on the request of" + sender)
            log("discord.log", sender + ', ')


client.run('')
