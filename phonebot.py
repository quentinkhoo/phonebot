
from dotenv import load_dotenv
import discord
import os
from datetime import datetime
import time

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# for testing reasons
TEST_CHANNEL_ID = 1401921828804493353
TEST_USER_ID = 210092278675537920

# our favourite
PHONE_USER_ID = 150641779794903040

GUILDS = ["Lilbitch", "EXTRA-PEACEFULL", "staging"]
GUILD_CHANNEL_IDS = [861425569887682620, 865560755138986014, TEST_CHANNEL_ID]

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

@client.event
async def on_presence_update(old_presence, new_presence):

  channel = client.get_channel(GUILD_CHANNEL_IDS[GUILDS.index(old_presence.guild.name)])
    
  if (new_presence.id == TEST_USER_ID):
    if (new_presence.activity != None and new_presence.activity.name == "Dota 2"):
      print(f"Phone started playing at {datetime.now()}")
      await channel.send("@everyone hello boys, come dotes don't dodge")

    if (old_presence.activity and old_presence.activity.name == "Dota 2"):
      print(f"Phone stopped playing at {datetime.now()}")
      await channel.send("@everyone i stop le, jiahui can turn off stream le")

client.run(BOT_TOKEN)