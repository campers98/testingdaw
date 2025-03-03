import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps.
API_ID = int(getenv("API_ID", "24086498"))
API_HASH = getenv("API_HASH", "0c459b186767a4634604c740c001c0c3")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("6066551482:AAH9CHuxNWc0qihY6qOfzIkmep6XdeD_SeE")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME","Soupboy_single")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "SvD_chatfight_bot")
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , "SVDMusicBot")
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME" , "Songjoker1")
EVALOP = list(map(int, getenv("EVALOP", "5259884546").split()))
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb://clve73lfu001ha4me1al6gw90:UTfT7DjJGjwyvbdXaM1hDrVj@104.251.218.202:9013/?readPreference=primary&ssl=false")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 20000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1001975251757))

# ------------------------------------------------
GPT_API = getenv("sk-proj-mywH9SfPWQuT2QhGLhKkT3BlbkFJUafYpIlrEpoYbz9rcy8L")
# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 655594746))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "github.com/campers98/testingdaw",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TeamHyperBOts")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Team_Hypers_Networks")


# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "0"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

# Ge@STRINGSEASO_NBOT2 session from @STRINGSEASO_NBOT
STRING1 = getenv("STRING_SESSION", "BQFvh-IAaOkBnrTD0HLoGiJwuqU4k7JHoxbP-dyyo2rQsbWu7aROO3IxsG7bbQ5A14OGM-eNu_ePJbP9ArPPvQmn9OflXXqtEa9TtgWRDfUOHOqGTIEXR47l_rw4TIHV6JdHf6KGFCXdmNMDtBQ0II_2AnIvOfoZSs2t5PP3AbOjZhT0vd63RMdIy3Qer2evKA8mQdRWmHvh3_eE23xqou_cfnAhNKGD8UcInDYz0-3UeAIkQdZwg-2haFgIitgiwZ4bm-JDLvm5HjjzDXJloRrTfN4DKCCrRxbHbLr1iSwWPWK-6nUiKfPXURTSH15bqTDme2hfK97SBCv4qQthuR30h_ilBwAAAAE5g3gCAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
AMBOT = [
    "🏹",
    "🦋",
    "🪁",
    "🧪",
    "🏏",
     "⚡️",
     "♥️🔥",
     "🎧",
     "🤡",
     "🕷",
     "🍷",
     "🐅",
     "🦜",
    "🚓",
    "🚬",
    "🧸",
    "✉️",
    "💀",
    "🔫",
    "🙂",
    "🕊️",
    "🤩",
    "🙂",
    "🥸",
    "🪄",
    "👀",
    "📎",
    "👀",
    "❤️‍🔥"
]
AMOP = ["ʜᴇʟʟᴏ {0}, 🌹\n\n ɪᴛ'ꜱ ᴍᴇ {1} !\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n٨♡ ᑭOᗯEᖇEᗪ♡ᗷY ♡٨ﮩ\n💙٨ [𝐇ʏᴘᴇʀ 𝐍ᴇᴛᴡᴏʀᴋ](https://t.me/Team_Hypers_Networks) ٨💙✯𖣔\n\n ᴄᴏɴᴛʀᴏʟʟᴇᴅ - [SVD](https://t.me/Soupboy_single)👻",
        "ʜɪɪ, {0} ~\n\n◆ ɪ'ᴍ ᴀ {1} ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ ꜱᴏᴍᴇ ᴜꜱᴇꜰᴜʟ\n◆ ᴜʟᴛʀᴀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ꜰᴇᴀᴛᴜʀᴇꜱ.\n\n✨ ꜰᴇᴀᴛᴜʀᴇꜱ ⚡️\n◆ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs.\n◆ Sᴜᴘᴇʀғᴀsᴛ ʟᴀɢ Fʀᴇᴇ ᴘʟᴀʏᴇʀ.\n◆ ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ + ᴠɪᴅᴇᴏ.\n◆ ʟɪᴠᴇ ꜱᴛʀᴇᴀᴍɪɴɢ.\n◆ ɴᴏ ᴘʀᴏᴍᴏ.\n◆ ʙᴇꜱᴛ ꜱᴏᴜɴᴅ Qᴜᴀʟɪᴛʏ.\n◆ 24×7 ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ.\n◆ ᴀᴅᴅ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴀᴅᴍɪɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴍᴜꜱɪᴄ 🎵.\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n٨♡ ᑭOᗯEᖇEᗪ♡ᗷY ♡٨ﮩ\n💙٨ [𝐇ʏᴘᴇʀ 𝐍ᴇᴛᴡᴏʀᴋ](https://t.me/Team_Hypers_Networks) ٨💙\n\nᴄᴏɴᴛʀᴏʟʟᴇᴅ - [SVD](https://t.me/Soupboy_single)👻",
        "ʜᴇʟʟᴏ {0}, 🌹\n\n ɪᴛ'ꜱ ᴍᴇ {1} !\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n٨♡ ᑭOᗯEᖇEᗪ♡ᗷY ♡٨ﮩ\n💙٨ [𝐇ʏᴘᴇʀ 𝐍ᴇᴛᴡᴏʀᴋ](https://t.me/Team_Hypers_Networks) ٨💙\n\nᴄᴏɴᴛʀᴏʟʟᴇᴅ - [SVD](https://t.me/Soupboy_single)👻",
        "𝓞𝓲𝓲 {0},\n ᴍʏ ꜱᴇʟꜰ {1} ..\n{1} ꜱʏꜱ ꜱᴛᴀᴛꜱ\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\nᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.\n\n٨♡ ᑭOᗯEᖇEᗪ♡ᗷY ♡٨ﮩ\n💙٨ [𝐇ʏᴘᴇʀ 𝐍ᴇᴛᴡᴏʀᴋ](https://t.me/Team_Hypers_Networks) ٨💙\n\nᴄᴏɴᴛʀᴏʟʟᴇᴅ - [SVD](https://t.me/Soupboy_single)👻",
        "ʜᴇʏ, {0} \nɪ'ᴍ {1},\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs.\n┠ ◆ ᴀʟʟ-ɪɴ-ᴏɴᴇ ʙᴏᴛ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ꜱᴏɴɢꜱ ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.\n┠ ◆ ʏᴏᴜ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ɪᴍᴀɢᴇs.\n┠ ◆ ʏᴏᴜ ᴄᴀɴ ᴛʀᴀɴꜱʟᴀᴛᴇ ᴍᴜʟᴛɪᴘʟᴇ ʟᴀɴɢᴜᴀɢᴇꜱ.\n┠ ◆ ɪ ᴄᴀɴ ᴍᴜᴛᴇ,ᴜɴᴍᴜᴛᴇ,ʙᴀɴ,ᴜɴʙᴀɴ,ᴋɪᴄᴋ..\n┠ ◆ ꜱᴘᴇᴄɪᴀʟ ᴡᴇʟᴄᴏᴍᴇ \n┠ ◆ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs ᴄʟɪᴄᴋ ᴄᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ...\n┗━━━━━━━━━━━━━━━━━⧫\n๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.\n\n٨♡ ᑭOᗯEᖇEᗪ♡ᗷY ♡٨ﮩ\n💙٨ [𝐇ʏᴘᴇʀ 𝐍ᴇᴛᴡᴏʀᴋ](https://t.me/Team_Hypers_Networks) ٨💙\n\nᴄᴏɴᴛʀᴏʟʟᴇᴅ - [SVD](https://t.me/Soupboy_single)👻"
       ]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}



START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/c7fc58423bbdac8159654.mp4"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/af9ce1fe9aeaa0a7fbdda.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/049da2a0678db379dc6ca.jpg"
STATS_IMG_URL = "https://telegra.ph/file/9349a004446e5e94abd6b.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/86f81220c410743f1e1b1.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/86f81220c410743f1e1b1.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/c281396ec344634c68351.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/ae29f79bef9e6f3ea8023.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/a89946fc5064191a82b97.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/563bd894a6903804c8646.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/2f2ad8bdeb3527c5501a0.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/bb5dcc863ee7da32dc832.jpg"



def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
