from ANNIEMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **Hey inga va veh nee** ",
           " **VE-NN-A thalaiya yena da pandra** ",
           " **Nalavaneee saptiya yenna pandra** ",
           " **deiii nee lam yen irruka poidu appdey heh😋** ",
           " **Nanae kolanthai da nambumga da** ",
           " **moodhugula knife yedhutu yara kuthulam nu partha yenna da nee vanthu nikuraa🙃** ",
           " **Ana solliten ithulam nalathuku illa parthukaa ! avalothan han🤨** ",
           " **Oru flow la poiturukum bothu yevan da athu nadula comedy pannikituu __ odddu** ",
           " **Ama onu vanganum heh yenna vangalam solluu🥲** ",
           " **dei murugesha antha AK47 gun ha konjam kooda bore adikuthu😋** ",
           " **yenna da suda matikuthi ! manichidu talaivarey bullet podala** ",
           " **athu yeppadey da yunna sudanum nu kekum bothu mattum bullet kanum🙄🤔** ",
           " **yunnaku yenna mooku neelama irrukam 🤔! pakathu theru la poster la irrunthuchhiii🏃🏃** ",
           " **Ana yunnaku vai irruke yennaku mela irruku 🙄🙄** ",
           " **sari yedhachum nalla song sollu kepom🫶** ",
           " **paatu poda sonna yena yen da podura ! venna thalaiya** ",
           " **yenna game thala aduva nee😛! oru match polama** ",
           " **Ama yunna pathi onu sonnangley ath uumnai ha🤔** ",
           " **sari yellame vithudu, nan oru 3 kelvi kekuren soluriya nu pakalam** ",
           " **yara nee neelam oru aley illaa venna thalaiya🤗** ",
           " **konjam kooda navura vidamatikuran heh yenna da venum yunnaku** ",
           " **Yevalo vati da sollurathu yunnaku mandai la brain heh illa da yunnaku venna thalaiya** ",
           " **Ana sathiyama sollala nee lam thiruntha mata🥺🥺** ",
           " **ama nan paitiyakaran na nee yaruu😶** ",
           " **yunnaku vekam lam vratha da sena panni marri nikuraa🤔** ",
           " **appadey ha ithu vera theriyaama pocha😜** ",
           " **amaa yenna alaiyee kanum sethutiya** ",
           " **nalla thingura yenna vitutu nalla irrpa** ",
           " **sari satu butu nu sollu yenna venum sapuda apram kasu illanu nu soliduven** ",
           " **Nee nalavana illna ketavanuku mela nalavn ha🙊** ",
           " **ama nee ipo yenna pandra yenna marri vetiya thane irrukaa apram yenga pore😺** ",
           " **sari sari pesunathu pothum poi toongu🥲** ",
           " **yepayum happy ha samthosama irru apo than yunna pakuravanga irruntha ivana marri irrukanum nu ninachi santhosama irrupanga😅** ",
           " **illana irrukura vanagalaiyum auchi irruka vidu da venna ythalaiya🙊🙊** ",
           " **Sooruu inga illaiyam pakathu veedu layum illaiyam agamothathuku sorru ilaiyam🙈🙈** ",
           " **porathum pore irru kuli kulla thali viduren🕳** ",
           " **sari apo nan kilamburen neeyum pesitu nalla urutitu poi toongu, thaniya da🙊** ",
           " **Nan nee avan avar ival iva yellarum ... onum illa..?👀** ",
           " **yelai anga yenna da pandra inga va game adalam** ",
           " **sari bore adicha sollu game adalam** ",
           " **inga oruthan irrupan nalla parru yunnakula irrukpan ana irrukamatan avan yar??😻** ",
           " **ama nee yaru sollu ?🙃** ",
           " **Ice Mittai Vangitariya ?🙊** ",
           " **oru game adalam who is up ?🙃** ",
           ]

VC_TAG = [" **⚘ আমাকে ভুলে যাও...💥**",
         " **⚘ আমি তোমাকে ভালোবাসি না...💥**",
         " **⚘ এটাকে তোমার করো পিয়া, তোমার করো...💥**",
         " **⚘ আমার গ্রুপেও যোগ দিন...💥**",
         " **⚘ আমি হৃদয়ে তোমার নাম রেখেছি...💥**",
         " **⚘ তোমার সব বন্ধু কোথায়...💥**",
         " **⚘ কার স্মৃতিতে তুমি হারিয়ে গেছো আমার ভালোবাসা...💥**",
         " **⚘ তোমার পেশা কি...💥**",
         " **⚘ তুমি কোথায় থাকো...💥**",
         " **⚘ শুভ সকাল, বাবু...💥**",
         " **⚘ শুভ রাত্রি, অনেক দেরি হয়ে গেছে...💥**",
         " **⚘ আমার আজ খুব খারাপ লাগছে...💥**",
         " **⚘ আমার সাথেও কথা বল...💥**",
         " **⚘ আজ রাতের খাবারের জন্য কি...💥**",
         " **⚘ কি হচ্ছে...💥**",
         " **⚘ তুমি মেসেজ দাও না কেন...💥**",
         " **⚘ আমি নির্দোষ...💥**",
         " **⚘ এটা গতকাল মজা ছিল, তাই না...💥**",
         " **⚘ তুমি গতকাল কোথায় ব্যস্ত ছিলে...💥**",
         " **⚘ তুমি কি সম্পর্কে আছো...💥**",
         " **⚘ তুমি খুব শান্ত থাকো বন্ধু...💥**",
         " **⚘ তুমি কি গাইতে জানো, গাইতে...💥**",
         " **⚘ তুমি কি আমার সাথে বেড়াতে আসবে...💥**",
         " **⚘ সবসময় হাসিখুশি থেকো বন্ধু...💥**",
         " **⚘ আমরা কি বন্ধু হতে পারি...💥**",
         " **⚘ তুমি কি বিবাহিত...💥**",
         " **⚘ এত দিন কোথায় ব্যস্ত ছিলে...💥**",
         " **⚘ লিঙ্ক বায়োতে আছে, এখন যোগ দিতে...💥**",
         " **⚘ মজা করলাম...💥**",
         " **⚘ আপনি কি এই গ্রুপের মালিককে চেনেন...💥**",
         " **⚘ তোমার কি কখনো মনে পড়ে আমায়...💥**",
         " **⚘ চলো পার্টি করি...💥**",
         " **⚘ আজ কেমন এলো...💥**",
         " **⚘ কেমন কাটলো তোমার দিন...💥**",
         " **⚘ তুমি কি দেখেছো...💥**",
         " **⚘ আপনি কি এখানকার প্রশাসক...💥**",
         " **⚘ আমরা বন্ধু হতে পারি...💥**",
         " **⚘ তুমি কি সম্পর্কে আছো...💥**",
         " **⚘ আর বন্দী কেমন আছে...💥**",
         " **⚘ তোমাকে গতকাল দেখেছি...💥**",
         " **⚘ তুমি কোথা থেকে...💥**",
         " **⚘ আপনি কি অনলাইনে আছেন...💥**",
         " **⚘ তুমি কি আমার বন্ধু....💥**",
         " **⚘ তুমি কি খেতে পছন্দ কর...💥**",
         " **⚘ আমাকে আপনার গ্রুপে অ্যাড করুন, আমি গান বাজিয়ে সবাইকে ট্যাগ করব....💥**",
         " **⚘ আজ আমি দুঃখিত...💥**",
         " **⚘ তুমি কি সত্য খেলবে এবং সাহস করবে...💥**",
         " **⚘ তোমার মত বন্ধু থাকলে চিন্তার কি আছে...💥**",
         " **⚘ কি হয়েছে তোমার...💥**",
         " **⚘ তুমি কি চকলেট খেতে চাও....💥**",
         " **⚘ হ্যালো বাবু...💥**",
         " **⚘ আমার সাথে চ্যাট করো...💥**",
         " **⚘ তুমি কি বলো...💥**"
        ]


@app.on_message(filters.command(["entag", "englishtag" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ithu thaan thavarana seyal, Niruvagi kitta kelunga (admins).... ")

    if message.reply_to_message and message.text:
        return await message.reply("Msg ah tag pannaatha. ,/entag  nu thaniya podu ve-nn-a...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("Msg ah tag pannaatha. ,//entag  nu thaniya podu ve-nn-a...")
    else:
        return await message.reply("Msg ah tag pannaatha. ,//entag  nu thaniya podu ve-nn-a...")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["bntag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ithu thaan thavarana seyal, Niruvagi kitta kelunga (admins)... ")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["cancel", "enstop", "bnstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ innum arambikave illa pangu.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ithu thaan thavarana seyal, Niruvagi kitta kelunga (admins).")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply(f"**Nee than niruthunatha**\n{message.from_user.mention}\n**Irrunga varen .. 🛵**")
          
