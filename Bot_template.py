import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix=';') #COMMAND PREFIX

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) #TELLS YOU IF THE BOT HAS CONNECTED
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Hello i am your discord bot')) #CREATES A BOT STATUS

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!') #BOT WILL REPEAT THIS

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms') #PING COMMAND

client.run('your token here')

#https://discordpy.readthedocs.io/en/latest/ - link to Discord.py