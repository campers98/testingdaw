import random

from pyrogram import Client, filters
from ANNIEMUSIC import app

# Dictionary of sticker packs
STICKER_PACKS = {
    "vadaki": [
        "CAACAgUAAxkBAAEMESlmOnc2p_-Rho2BNpdADaQKxW8SlAAC4woAAvhuAVbL3lwuysuYijUE"
        # Add more sticker URLs as needed
    ],
    # You can define more sticker packs in a similar manner
}

  @app.on_message(filters.command("vadaki") & ~filters.forwarded & ~filters.via_bot)
def slap_command(client, message):
    try:
        sender = message.from_user.mention(style='markdown')

        target = sender if not message.reply_to_message else message.reply_to_message.from_user.mention(style='markdown')

        msg = f"{sender} Sunil bhaaaaai  {target}! 🙊"

        # Select a random sticker URL from the specified sticker pack
          random_sticker_url = random.choice(STICKER_PACKS["vadaki"])

        message.reply_sticker(sticker=random_sticker_url, quote=True, caption=msg)
        
    except Exception as e:
        message.reply_text(f"An unexpected error occurred: {str(e)}")
