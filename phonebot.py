
from dotenv import load_dotenv
import discord
import os
import datetime
import time

is_testing = True

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# for testing reasons
TEST_CHANNEL_ID = 1401921828804493353
#254827519352504321
TEST_USER_ID = 254827519352504321

# our favourite
PHONE_USER_ID = 150641779794903040

GUILDS = ["Lilbitch", "EXTRA-PEACEFULL", "staging"]
GUILD_CHANNEL_IDS = [861425569887682620, 865560755138986014, TEST_CHANNEL_ID]
VOICE_CHANNEL_ID = 1401921764161749006

AUDIO_FILE = "gogogo.mp3"

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')


@client.event
async def on_presence_update(old_presence, new_presence):

  if is_testing:
    channel = client.get_channel(TEST_CHANNEL_ID)
  else:
    channel = client.get_channel(GUILD_CHANNEL_IDS[GUILDS.index(old_presence.guild.name)])
    
  if (new_presence.id == TEST_USER_ID):
    if (new_presence.activity != None and new_presence.activity.name == "Dota 2"):
      print(f"Phone started playing at {datetime.datetime.now()}")
      await channel.send("@everyone hello boys, come dotes don't dodge")

    if (old_presence.activity and old_presence.activity.name == "Dota 2"):
      print(f"Phone stopped playing at {datetime.datetime.now()}")
      await channel.send("@everyone i stop le, jiahui can turn off stream le")


@client.event
async def on_voice_state_update(member, before, after):
    # Check if it's the target user joining a voice channel
    if member.id == TEST_USER_ID and before.channel is None and after.channel is not None:
        print(f'{member.name} joined {after.channel.name}')
        
        voice_channel = after.channel
        vc = await voice_channel.connect()

        # Play the audio
        if not vc.is_playing():
            # vc.play(discord.FFmpegPCMAudio(AUDIO_FILE), after=lambda e: print("Finished playing"))
            vc.play(RawPCMAudio("gogogo.pcm"), after=lambda e: print("Finished playing"))
        
        # Leave after playback
        while vc.is_playing():
            await discord.utils.sleep_until(discord.utils.utcnow() + datetime.timedelta(seconds=0.1))
        await vc.disconnect()


class RawPCMAudio(discord.AudioSource):
    def __init__(self, file_path):
        self.file = open(file_path, 'rb')

    def read(self):
        return self.file.read(3840)  # 20ms of PCM at 48kHz 16-bit stereo

    def is_opus(self):
        return False


client.run(BOT_TOKEN)