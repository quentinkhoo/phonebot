
from dotenv import load_dotenv
import discord
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
print(BOT_TOKEN)

# for testing reasons
TEST_CHANNEL_ID = 1401921828804493353
TEST_USER_ID = 210092278675537920

# #dota2 news feed
CHANNEL_ID = 861425569887682620
# our favourite
PHONE_USER_ID = 150641779794903040

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

  channel = client.get_channel(TEST_CHANNEL_ID)
    
  if (new_presence.id == TEST_USER_ID):
    if (new_presence.activity != None and new_presence.activity.name == "Dota 2"):
      await channel.send('@everyone phone is online on dota boys!')

    if (new_presence.activity == None and old_presence.activity.name == "Dota 2"):
      await channel.send('@everyone phone stop playing le, can finally win')


client.run(BOT_TOKEN)