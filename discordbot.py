import os
import discord
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()


@client.event
async def on_ready():
    print("Success login")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '/neko':
        await message.channel.send('Meow')

    if client.user in message.mentions:
        reply = f'{message.author.mention} 呼んだ？'
        await message.channel.send(reply)

client.run(TOKEN)
