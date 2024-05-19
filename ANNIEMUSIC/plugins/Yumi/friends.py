from pyrogram import Client, filters
import random
from ANNIEMUSIC import app

def get_random_message(friendship_percentage, gender_combo):
    if friendship_percentage <= 30:
        return ("Friendship is budding but needs more nurturing.", None)
    elif friendship_percentage <= 70:
        return ("A strong friendship is forming. Keep nurturing it.", None)
    else:
        if gender_combo == "male_female":
            return ("Wow! A beautiful friendship is blossoming between a boy and a girl!", get_random_gif("mixed"))
        elif gender_combo == "female_female":
            return ("Girls' friendship is forever!", get_random_gif("female"))
        elif gender_combo == "male_male":
            return ("Boys' friendship rocks!", get_random_gif("male"))

def get_random_gif(gender):
    if gender == "mixed":
        gifs = [
            "https://telegra.ph/file/75d3fab553b0c77b14b05.mp4",  # Mixed Friendship GIF 1
            "https://telegra.ph/file/8acb8e620639a362f0a50.mp4",  # Mixed Friendship GIF 2
            "https://telegra.ph/file/9534405519cb31d028a12.mp4",  # Mixed Friendship GIF 3
        ]
    elif gender == "female":
        gifs = [
            "https://telegra.ph/file/f4bc092fff04134f7b572.mp4",  # Female Friendship GIF 1
            "https://telegra.ph/file/93aa537ce89df67374895.mp4",  # Female Friendship GIF 2
            "https://telegra.ph/file/05ead3bab765eb867b5a9.mp4",  # Female Friendship GIF 3
        ]
    elif gender == "male":
        gifs = [
            "https://telegra.ph/file/4ff52b1cdec57fcef2730.mp4",  # Male Friendship GIF 1
            "https://telegra.ph/file/86cffbc62e4f0a624953d.mp4",  # Male Friendship GIF 2
            "https://telegra.ph/file/a38668e400e54eed16c5d.mp4",  # Male Friendship GIF 3
        ]
    return random.choice(gifs)
        
@app.on_message(filters.command("friends", prefixes="/"))
def friendship_command(client, message):
    command, *args = message.text.split(" ")
    if len(args) >= 2:
        friend1 = args[0].strip()
        friend2 = args[1].strip()
        
        # Gender classification (For simplicity, let's assume names ending with 'a' are female)
        gender_friend1 = "female" if friend1.lower().endswith("a") else "male"
        gender_friend2 = "female" if friend2.lower().endswith("a") else "male"
        
        friendship_percentage = random.randint(10, 100)
        
        # Determine the gender combination of the names
        if gender_friend1 != gender_friend2:
            gender_combo = "male_female"
        elif gender_friend1 == "female":
            gender_combo = "female_female"
        else:
            gender_combo = "male_male"
        
        friendship_message, friendship_gif = get_random_message(friendship_percentage, gender_combo)

        response = f"{friend1} 👫 {friend2}\n\nFriendship Compatibility: {friendship_percentage}%\n\n{friendship_message}"
        if friendship_gif:
            app.send_animation(message.chat.id, friendship_gif)
    else:
        response = "Please enter two names after /friends command."
    app.send_message(message.chat.id, response)
