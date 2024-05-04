import requests
from ANNIEMUSIC import app
from pyrogram import Client, filters

JOKE_API_ENDPOINT = 'https://v2.jokeapi.dev/'

@app.on_message(filters.command("hjoke"))
async def joke(_, message):
    response = requests.get(JOKE_API_ENDPOINT)
    r = response.json()
    joke_text = r['jokeContent']
    await message.reply_text(joke_text)
