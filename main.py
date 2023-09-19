import discord
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def getCep(cep):
    response = requests.get("https://ws.apicep.com/cep.json?code=" + cep)
    json_data = json.loads(response.text)
    return (json_data)


intents = discord.Intents.default()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Seu bot está logado como: {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!bv'):
        print("Chamou")
        await message.channel.send(f'Bem-vindo ao canal! Eu sou o {client.user}')

    if message.content.startswith('!inspire'):
        await message.channel.send(get_quote())

    if message.content.startswith('!oi'):
        await message.channel.send('Olá, seja bem-vindo ' + message.author.name)

    if message.content.startswith('!game'):
        await message.channel.send('Eae bucetudo, vamos jogar ?')

    if message.content.startswith("!cep"):
        vCep = message.content
        quote = getCep(vCep[5:])
        await message.channel.send(quote)


client.run(os.getenv('TOKEN2'))
