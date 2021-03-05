import discord
import requests
import os

_DISCORD_TOKEN = os.getenv("TOKEN")
_CATS_API_KEY = os.getenv("CAT_API")
cats_url = "https://api.thecatapi.com/v1/images/search?limit=1&size=small&mime_types=jpg,png"

def get_image(user):
    response = requests.get(f"{cats_url}&sub_id={user}", headers={"x-api-key": "e35526e7-d4cb-49ee-a53d-774265c47598"})
    return response.json()

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have loged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!Kiss?") or message.content.startswith("!kiss?"):
        image_info = get_image(message.author)
        await message.channel.send(image_info[0]["url"])

client.run(_DISCORD_TOKEN)