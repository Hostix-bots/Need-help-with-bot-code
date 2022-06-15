import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix=',', intents = discord.Intent.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("OTgzNzk3ODkyMjEwODg0NjM4.GBDshm.L4lbRKInYtgS0aZZ-sp1Ws3xFjHC_YMajbVOmU")
