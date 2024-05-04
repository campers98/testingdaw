from pyrogram import Client, filters
from pyrogram.types import Message
from ANNIEMUSIC import app

@app.on_message(filters.command("groupinfo", prefixes="/"))
async def get_group_status(_, message: Message):
    if len(message.command) != 2:
        await message.reply("Please provide a group username. Example: `/groupinfo YourGroupUsername`")
        return
    
    group_username = message.command[1]
    
    try:
        group = await app.get_chat(group_username)
    except Exception as e:
        await message.reply(f"Error: {e}")
        return
    
    total_members = await app.get_chat_members_count(group.id)
    group_description = group.description
    premium_acc = banned = deleted_acc = bot = 0  # You should replace these variables with actual counts.

    response_text = (
        f"──⇌••⇋__ ──⇌••⇋── __──⇌••⇋──\n\n"
        f"❁ デ︻ вαѕє ηαмє ︻デ : {group.title}               ℍ  \n"
        f"❁ デ︻  вαѕє ι∂  ︻デ : {group.id}                  𝕐   \n"
        f"❁ デ︻  ρяєѕєηт  ︻デ: {total_members}              ℙ  \n"
        f"❁ デ︻ gяσυρ вισ ︻デ: {group_description or 'N/A'} 𝔼  \n"
        f"❁ デ︻  υѕєяηαмє ︻デ : @{group_username}           ℝ   \n"
       
        f"➖➖🔉𖤍[🂱 𝐇𝐘𝐏𝐄𝐑 𝐍𝐞𝐭𝐖𝐨𝐫𝐊𝐬 🂱](https://t.me/TeamHyperNetworks)...🔉➖➖➖➖➖"
    )
    
    await message.reply(response_text)






# Command handler to get group status
@app.on_message(filters.command("status") & filters.group)
def group_status(client, message):
    chat = message.chat  # Chat where the command was sent
    status_text = f"‿❀ Group ID ‿❀: {chat.id}\n" \
                  f"‿❀   Title  ‿❀: {chat.title}\n" \
                  f"‿❀    Type  ‿❀: {chat.type}\n"
                  
    if chat.username:  # Not all groups have a username
        status_text += f"‿❀ Username ‿❀: @{chat.username}"
    else:
        status_text += "Username: None"

    message.reply_text(status_text)


#########
