import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
from discord.commands import slash_command

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

activity = discord.Activity(type=discord.ActivityType.playing, name="mit Keksen") # hier kannst du den Status ändern

bot = discord.Bot(intents=intents, debug_guilds=None, activity=activity)

@bot.event
async def on_ready():
    print("Dein Spambot ist nun ready! Code by: LeonMT1#6088")

@bot.event
async def on_message(message):
    await message.channel.send("Spam") # hier kannst du den text ändern was der bot spammen soll
    
if __name__== "__main__":
    load_dotenv()
    bot.run(os.getenv("TOKEN")) # erstelle eine .env Datei und schreibe da "TOKEN = (dein token)"
