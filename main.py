import discord
import requests
import os

_DISCORD_TOKEN = os.getenv("TOKEN")
_CATS_API_KEY = os.getenv("CAT_API")
_CRYPTO_API_KEY = os.getenv("CRYPTO_API")
cats_url = "https://api.thecatapi.com/v1/images/search?limit=1&size=small&mime_types=jpg,png&category=7,4,2,1,5"


def get_image(user):
    response = requests.get(f"{cats_url}&sub_id={user}",
                            headers={"x-api-key": _CATS_API_KEY})
    return response.json()

def get_doge():
    response = requests.get(" https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=74", headers={"X-CMC_PRO_API_KEY": _CRYPTO_API_KEY})
    if(response.status_code == 200)
        json = response.json()
        value = json["data"]["74"]["quote"]["USD"]["price"]
        message = f"The current value of Dogecoin is {value:.4f}"
    else:
        message = "Whoops! Cannot contact the Crypto server right now. Try again later"
    return message

client = discord.Client()


@client.event
async def on_ready():
    print(f"We have loged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content
    if content.startswith("!Kiss?") or content.startswith("!kiss?"):
        image_info = get_image(message.author)
        await message.channel.send(image_info[0]["url"])
    elif content.startswith("!bippy?"):
        await message.channel.send(
            "https://www.youtube.com/watch?v=jamjHQ_V_dQ")
    elif content.startswith("!bonk?"):
        mentions = message.mentions
        if len(mentions) > 0:
            channel = message.guild.afk_channel
            user = mentions[0]
            await user.move_to(channel, reason=f"{message.author} moved them for the memes!")

        elif len(mentions) > 1:
            await message.channel.send(
                "you may currently only bonk one user at a time")
        else:
            await message.channel.send(
                "you must mention the user you wish to bonk")
    elif content.startswith("!doge?"):
        doge_message = get_doge()
        await message.channel.send(doge_message)

    elif content.startswith("!banish?"):
        if len(mentions) > 0:
            user = mentions[0]
            await user.move_to(None,  reason=f"{message.author} moved them for the memes!")

        elif len(mentions) > 1:
            await message.channel.send(
                "you may currently only banish one user at a time")
        else:
            await message.channel.send(
                "you must mention the user you wish to banish")

    elif content.startswith("!help?"):
        help_info = "'!Kiss?' or '!kiss' to send a random cat image\n'!bippy?' to send the bippy video\n'!bonk? @user_mention' to send user to horny jail'\n'!banish? @user_mention' to disconnnect a user\n!doge? will return the current value of Dogecoin to 4 decimal places"
        await message.channel.send(help_info)


client.run(_DISCORD_TOKEN)
