from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ANNIEMUSIC import app
from ANNIEMUSIC.core.call import JARVIS
from ANNIEMUSIC.utils import bot_sys_stats
from ANNIEMUSIC.utils.decorators.language import language
from ANNIEMUSIC.utils.inline import supp_markup
from config import BANNED_USERS
import aiohttp
import asyncio
from io import BytesIO
from PIL import Image, ImageEnhance  # Add these imports

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())

    # Open the image using PIL
    carbon_image = Image.open(image)

    # Increase brightness
    enhancer = ImageEnhance.Brightness(carbon_image)
    bright_image = enhancer.enhance(1.7)  # Adjust the enhancement factor as needed

    # Save the modified image to BytesIO object with increased quality
    output_image = BytesIO()
    bright_image.save(output_image, format='PNG', quality=100)  # Adjust quality as needed
    output_image.name = "carbon.png"
    return output_image

@app.on_message(filters.command("toe", prefixes=["/", "!",]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    PING_IMG_URL = "https://telegra.ph/file/5a4b3b782cb0257dca491.jpg"
    captionss = "**💻 𝗖𝗮𝗹𝗹𝗶𝗻𝗴 𝘁𝗵𝗲 𝗦𝗲𝗿𝘃𝗲𝗿 𝗣𝗿𝗼𝘁𝗼𝗰𝗼𝗹.**"
    response = await message.reply_photo(PING_IMG_URL, caption=(captionss))
    await asyncio.sleep(1)
    await response.edit_caption("**🙀𝗥𝗲𝗾𝘂𝗲𝘀𝘁𝗶𝗻𝗴 𝗼𝗻 𝘁𝗵𝗲 𝘀𝗲𝗿𝘃𝗲𝗿..**")
    await asyncio.sleep(1)
    await response.edit_caption("**🤐𝗛𝘆𝗽𝗲𝗿 𝗶𝘀 𝗘𝘅𝘁𝗿𝗮𝗰𝘁𝗶𝗻𝗴 𝗧𝗵𝗲 𝗗𝗮𝘁𝗮**")
    await asyncio.sleep(1)
    await response.edit_caption("**🤫𝗛𝘆𝗽𝗲𝗿 𝗶𝘀 𝗳𝘂𝗹𝗹 𝗼𝗳 𝗯𝗼𝘆𝘀 - 𝗦𝗶𝗴𝗵𝘀𝗲𝗲𝗶𝗻𝗴 𝘁𝗵𝗲 𝗚𝗶𝗿𝗹𝘀..**")
    await asyncio.sleep(1.5)
    await response.edit_caption("**☠️𝗛𝘆𝗽𝗲𝗿 𝗶𝘀 𝗨𝗽𝗴𝗿𝗮𝗱𝗶𝗻𝗴 𝘁𝗵𝗲 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲...**")
    await asyncio.sleep(1.5)
    await response.edit_caption("**😍𝗛𝘆𝗽𝗲𝗿 𝗡𝗲𝘁𝘄𝗼𝗿𝗸 𝗶𝘀 𝗰𝗿𝗲𝗮𝘁𝗲𝗱....**")
    await asyncio.sleep(1.5)
    await response.edit_caption("**𝗧𝗵𝗲 𝗧𝗲𝗮𝗺 𝗜𝘀 𝗪𝗼𝗿𝗸𝗶𝗻𝗴 𝗢𝗻 𝗕𝘂𝗶𝗹𝗱𝗶𝗻𝗴 𝗧𝗵𝗲 𝗡𝗲𝘁𝘄𝗼𝗿𝗸𝘀 🤧 !**")
    await asyncio.sleep(2)
    await response.edit_caption("**𝘁𝗵𝗲 𝗡𝗲𝘁𝘄𝗼𝗿𝗸 𝗶𝘀 𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝘁𝗵𝗲 𝗙𝗶𝗹𝗲𝘀..𝗕𝗲 𝗣𝗮𝘁𝗶𝗲𝗻𝘁 𝟯.. 𝟮.. 𝟭...**")
    start = datetime.now()
    pytgping = await JARVIS.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    text =  _["ping_2"].format(resp, app.name, UP, RAM, CPU, DISK, pytgping)
    carbon = await make_carbon(text)
    captions = "**👹 𝐇ʏᴘᴇʀ  𝐍ᴇᴛᴡᴏʀᴋ🕷\nㅤ  🦜👀ᴄᴀᴛᴄʜ..ᴛʜᴇ..sᴛᴀᴛs..ʙʏ..ᴛʜᴇ..ᴛᴏᴇ🫣💞**"
    await message.reply_photo((carbon), caption=captions,
    reply_markup=InlineKeyboardMarkup(
            [
                [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="✦ ɢʀᴏᴜᴘ ✦", url=f"https://t.me/Team_Hypers_Networks",
            ),
            InlineKeyboardButton(
                text="✧ ᴍᴏʀᴇ ✧", url=f"https://t.me/TeamHyperBOts",
            )
        ],
        [
            InlineKeyboardButton(
                text="❅ ʜᴇʟᴘ ❅", callback_data="settings_back_helper"
            )
        ],
    ]
    ),
        )
    await response.delete()
