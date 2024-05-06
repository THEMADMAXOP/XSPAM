from telethon import __version__, events, Button

from config import X1, OWNER_ID


START_BUTTON = [
    [
        Button.url("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", "https://t.me/MADMAX_SPAM_BOT?startgroup=true")
    ],
    [
        Button.inline("ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs", data="help_back")
    ],
    [
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/VOICEOFHEART0"),
        Button.url("ʀᴇᴘᴏ", "https://github.com/THEMADMAXPRO/XSPAM")
    ],
    [
        Button.url("ᴍᴀᴅᴍᴀx", "https://t.me/sashikant_xd"),
    ]
]


@X1.on(events.NewMessage(pattern="/sstart"))
async def start(event):              
    if event.is_private:
        Altbot = await event.client.get_me()
        bot_name = Altbot.first_name
        bot_id = Altbot.id
        TEXT = f"**❖ ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}), ᴡᴇʟᴄᴏᴍᴇ ʙᴀʙʏ.\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n● ɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id}) ʙᴏᴛ.**\n\n"
        TEXT += f"● **xʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ ➥** `M3.9/V8`\n"
        TEXT += f"● **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ➥** `3.11.8`\n"
        TEXT += f"● **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ➥** `{__version__}`\n\n"
        TEXT += f"❖ **ᴛʜɪs ɪs ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ ᴍᴀᴅᴍᴀx sᴘᴀᴍ ʙᴏᴛ ғᴏʀ ɴᴏɴ sᴛᴏᴘ sᴘᴀᴍᴍɪɴɢ.**"
        await event.client.send_file(
                    event.chat_id,
                    "https://te.legra.ph/file/c687602a4c2ac3afa7ee1.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
      )
