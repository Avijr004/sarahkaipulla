from ShizukaXMusic import app
import asyncio
import random
from pyrogram import Client, filters
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

TAGMES = [ " **I love you 🤗** "
           " **neeium nanum sernthae pogum neramae** "
           " **road la iruku pallam neetha en chellam** "
           " **aii nee en idupa patha na atha patha** "
           " **na pothuva kova pada mata ena kova pada vachiratha** "
           " **ne en ivlo gundaaaaa iruka** "
           " **ne loosa ila loosu mathiri nadikuriya** "
           " **pls call the ambulance unga kannu ena shoot panidichu** "
           " **canteen la ituku pufs uh unaku enaku luvs uh** "
           " **nalla shaving pana mala korangu mathiri oru munji** "
           " **uthu pakatha vekama iruku** "
           " **una pethangsla ila senjangala** "
           " **ne ena mulla una thotalae kuthuthu** "
           " **thambi tea inu varala** "
           " **nalla saptu saptu thadi maadu Mathiri iruka** "
           " **i think I'm fall in love with you** "
           " **night lam thukamae varala neetha vara** "
           " **kolantha poi paal kudichitu thungu po** "
           " **epa pathalu urutite iru Vera vela ila la** "
           " **na unaku frnd ah kedaika ne kuduthu vachirukanu** "
           " **ne ena puliya** "
           " **enkuda pesa matiya** "
           " **en eee nu palla katura** "
           " **unkuda ma doo** "
           " **enkuda pesa matiya** "
           " **ne romba cute ah iruka** "
           " **sumave iruka matiya** "
           " **aama yar ne** "
           " **enaku pasikuthu** "
           " **na unaku oru paatu padava** "
           " **unkita onu solanu** "
           " **na unaku yaru** "
           " **una la thiruthave mudiyathu** "
           " **ne la human thana doubt ah iruku** "
           " **en mela pasame ila unaku** "
           " **ne urutu un nalla manasuku neetha jeipa** "
           " **you buffalo** "
           " **pae** "
           " **pani** "
           " **eruma adi venuma** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
           " **** "
         
         ]

@app.on_message(filters.command(["tagall", "all", "tagmember"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        return await message.reply("This command can be used in groups and channels!")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("**ᴏɴʟʏ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ!**")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall hello 👈** ᴛʀʏ ᴛʜɪs ɴᴇxᴛ ᴛɪᴍᴇ ғᴏʀ ᴛᴀɢɢɪɴɢ...*")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall hii 👈 **ᴛʀʏ ᴛʜɪs ᴏʀ ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ...**")
    else:
        return await message.reply("/tagall hii 👈 **ᴛʀʏ ᴛʜɪs ᴏʀ ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ...**")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_chat_members(chat_id):
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

@app.on_message(filters.command(["cancel", "stop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("**ɴᴏ ᴀᴄᴛɪᴠᴇ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss ɪs sᴛᴀʀᴛᴇᴅ ʙʏ ᴍᴇ...**")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs. ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ...**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("**ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss sᴛᴏᴘᴘᴇᴅ**")
