from io import BytesIO

import discord
import logging
import requests

from conf import TOKEN

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


class YLBotClient(discord.Client):
    async def on_ready(self):
        logger.info(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            logger.info(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if 'кот' in message.content.lower():
            url = requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url']
            arr = BytesIO(requests.get(url).content)
            file = discord.File(fp=arr, filename=url.split('/')[-1])
            await message.channel.send("Лови котяру", file=file)

        if 'cобак' in message.content.lower() or 'бобик' in message.content.lower():
            url = requests.get('https://dog.ceo/api/breeds/image/random').json()['message']
            arr = BytesIO(requests.get(url).content)
            file = discord.File(fp=arr, filename=url.split('/')[-1])
            await message.channel.send("вот бобик", file=file)


intents = discord.Intents.default()
intents.members = True
client = YLBotClient(intents=intents)
client.run(TOKEN)