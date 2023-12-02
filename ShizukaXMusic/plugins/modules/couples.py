import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType

from ShizukaXMusic.utils.database import get_couple, save_couple
from ShizukaXMusic import pbot
from ShizukaXMusic import app

# Date and time
def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    dt_list = dt_string.split(" ")
    return dt_list


def dt_tom():
    a = (
        str(int(dt()[0].split("/")[0]) + 1)
        + "/"
        + dt()[0].split("/")[1]
        + "/"
        + dt()[0].split("/")[2]
    )
    return a


today = str(dt()[0])
tomorrow = str(dt_tom())


@app.on_message(filters.command(["couple", "couples"]))
async def couple(_, message):
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply_text("This command only works in groups.")
    try:
        user_id = message.chat.id
        is_selected = await get_couple(user_id, today)
        if not is_selected:
            list_of_users = []
            async for i in app.get_chat_members(message.chat.id, limit=50):
                if not i.user.is_bot:
                    list_of_users.append(i.user.id)
            if len(list_of_users) < 2:
                return await message.reply_text("Not enough users")
            c1_id = random.choice(list_of_users)
            c2_id = random.choice(list_of_users)
            while c1_id == c2_id:
                c1_id = random.choice(list_of_users)
            c1_mention = (await app.get_users(c1_id)).mention
            c2_mention = (await app.get_users(c2_id)).mention

            couple_selection_message = f"""**Today beauties 🙈🙊**

{c1_mention} + {c2_mention} = 😘
__New couple of the day can be chosen at 12AM {tomorrow}__"""
            await app.send_message(message.chat.id, text=couple_selection_message)
            couple = {"c1_id": c1_id, "c2_id": c2_id}
            await save_couple(user_id, today, couple)

        elif is_selected:
            photo_url = ["https://telegra.ph/file/66a26cca7186e4f21629d.jpg",
                         "https://telegra.ph/file/afa3b15a82cc655ee8d7d.jpg",
                         "https://telegra.ph/file/332f284b35e07babcd58a.jpg",
                         "https://telegra.ph/file/a3ba3cf91dc6f3f29bc9a.jpg",
                         "https://telegra.ph/file/8bad877b564bca0dc331a.jpg",
                         "https://telegra.ph/file/048633ac735cce7eb0886.jpg",
                         "https://telegra.ph/file/7c9a0debcb09fa4444753.jpg"
                       ]
                   
            await message.reply_photo == random.choice(photo=photo_url)
            c1_id = int(is_selected["c1_id"])
            c2_id = int(is_selected["c2_id"])
            c1_name = (await app.get_users(c1_id)).mention
            c2_name = (await app.get_users(c2_id)).mention
            couple_selection_message = f"""Today beauties 🙈🙊

{c1_name} + {c2_name} = 😘
__New couple of the day can be chosen at 12AM {tomorrow}__"""
            await app.send_message(message.chat.id, text=couple_selection_message)
    except Exception as e:
        print(e)
        await message.reply_text(e)


__help__ = """
Choose couples in your chat

 ❍ /couple *:* Choose 2 users and send their name as couples in your chat.
"""

__mod_name__ = "Cᴏᴜᴘʟᴇ"
