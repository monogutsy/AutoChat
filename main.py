import discord
from discord.ext import commands, tasks
import os
import webserver

DISCORD_TOKEN = os.environ['discordkey']
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID = 1075695140410232846  # replace with your channel ID

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    send_hi.start()  # start the loop when bot is ready

@tasks.loop(minutes=10)
async def send_hi():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("*hi")

webserver.keep_alive()
bot.run("DISCORD_TOKEN")
