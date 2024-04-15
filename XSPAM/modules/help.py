from telethon import events, Button

from config import X1, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"**✦ ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ꜰᴏʀ xsᴘᴀᴍ ʜᴇʟᴘ ⏤͟͟͞͞★**"

HELP_BUTTON = [
    [
      Button.inline("ꜱᴘᴀᴍ", data="spam"),
      Button.inline("ʀᴀɪᴅ", data="raid")
    ],
    [
      Button.inline("ᴇxᴛʀᴀ", data="extra")
    ],
    [
      Button.url("ᴜᴘᴅᴀᴛᴇl", "https://t.me/STATUSDAIRY2"),
      Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/VOICEOFHEART0")
    ]
  ]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://te.legra.ph/file/c687602a4c2ac3afa7ee1.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(e)}")


extra_msg = f"""
**» ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗨𝘀𝗲𝗿𝗕𝗼𝘁: **ᴜꜱᴇʀʙᴏᴛ ᴄᴍᴅꜱ**
  1) {hl}ping 
  2) {hl}reboot
  3) {hl}sudo <reply to user>  --> Owner Cmd
  4) {hl}logs --> Owner Cmd

𝗘𝗰𝗵𝗼: **ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ**
  1) {hl}echo <reply to user>
  2) {hl}rmecho <reply to user>

𝗟𝗲𝗮𝘃𝗲: **ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ**
  1) {hl}leave <group/chat id>
  2) {hl}leave : Type in the Group bot will auto leave that group


**© @SASHIKANT_XD**
"""

                 
raid_msg = f"""
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗥𝗮𝗶𝗱: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.**
  1) {hl}raid <count> <username>
  2) {hl}raid <count> <reply to user>

𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}rraid <replying to user>
  2) {hl}rraid <username>

𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}drraid <replying to user>
  2) {hl}drraid <username>

𝐌𝐑𝐚𝐢𝐝: **ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}mraid <count> <username>
  2) {hl}mraid <count> <reply to user>

𝐒𝐑𝐚𝐢𝐝: **ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}sraid <count> <username>
  2) {hl}sraid <count> <reply to user>

𝐂𝐑𝐚𝐢𝐝: **ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}craid <count> <username>
  2) {hl}craid <count> <reply to user>


**© @SASHIKANT_XD**
"""

spam_msg = f"""
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗦𝗽𝗮𝗺: **ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ.**
  1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
  2) {hl}spam <count> <replying any message>

𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺: **ᴘᴏʀᴍᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ.**
  1) {hl}pspam <count>

𝗛𝗮𝗻𝗴: **ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ.**
  1) {hl}hang <counter>


** © @SASHIKANT_XD**
"""                     
           
           
@X1.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline("ꜱᴘᴀᴍ", data="spam"),
                Button.inline("ʀᴀɪᴅ", data="raid")
              ],
              [
                Button.inline("ᴇxᴛʀᴀ", data="extra")
              ],
              [
                Button.url("ᴜᴘᴅᴀᴛᴇ", "https://t.me/STATUSDAIRY2"),
                Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/VOICEOFHEART0")
              ]
            ]
          )
    else:
        await event.answer("ᴘᴇʜʟᴇ ᴍᴀᴅᴍᴀx ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ ʟᴀᴜᴅᴇ", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("◁", data="help_back"),],],
              ) 
    else:
        await event.answer("ᴘᴇʜʟᴇ ᴍᴀᴅᴍᴀx ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ ʟᴀᴜᴅᴇ", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("◁", data="help_back"),],],
          )
    else:
        await event.answer("ᴘᴇʜʟᴇ ᴍᴀᴅᴍᴀx ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ ʟᴀᴜᴅᴇ", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("◁", data="help_back"),],],
            )
    else:
        await event.answer("ᴘᴇʜʟᴇ ᴍᴀᴅᴍᴀx ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ ʟᴀᴜᴅᴇ", cache_time=0, alert=True)
