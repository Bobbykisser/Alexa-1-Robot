from telethon import events, Button, custom
import re, os
from MashaRoBot.events import register
from MashaRoBot import telethn as tbot
from MashaRoBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/1827ec3f0fd066a7c2874.jpg"
@register(pattern=("/alive"))
async def awake(event):
  WOLFX = event.sender.first_name
  WOLFX = "**🐺 𝐈 𝐀𝐦, 𝐖𝐨𝐥𝐟𝐗 ⚔️** \n\n"
  WOLFX += "**🐺 𝐖𝐨𝐥𝐟𝐗 𝐈𝐬 𝐏𝐞𝐫𝐟𝐞𝐜𝐭𝐥𝐲 𝐇𝐨𝐰𝐥𝐢𝐧𝐠**\n\n"
  WOLFX += "**🐺 𝐖𝐨𝐥𝐟𝐗 : 2.0 𝐋𝐀𝐓𝐄𝐒𝐓**\n\n"
  WOLFX += "**🐺 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫 :** [Hᴀᴄᴋᴇʀ 888+](https://t.me/HMF_OWNER_1)\n\n"
  WOLFX += "**🐺 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : 1.23.0**\n\n"
  BUTTON = [[Button.url("𝐒𝐔𝐏𝐏𝐎𝐑𝐓🗡️", "https://t.me/wolfxbotz"), Button.url("𝐔𝐏𝐃𝐀𝐓𝐄👨‍💻", "https://t.me/joinchat/r9qx47U5xEZjY2E1")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=WOLFX,  buttons=BUTTON)
