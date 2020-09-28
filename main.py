import os
from classes.noosClient import NoosClient

import discord
from dotenv import load_dotenv

load_dotenv('.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')


client = NoosClient()
client.run(TOKEN)
