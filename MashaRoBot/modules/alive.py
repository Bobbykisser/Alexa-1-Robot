from telethon import events, Button, custom
import re, os
from MashaRoBot.events import register
from MashaRoBot import telethn as tbot
from MashaRoBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/1827ec3f0fd066a7c2874.jpg"
@register(pattern=("/alive"))
async def awake(event):
  SERENA = event.sender.first_name
  SERENA = "**♡ I,m Lovely💕** \n\n"
  SERENA += "**♡ I'm Working with awesome speed**\n\n"
  SERENA += "**♡ Lovely : 2.0 LATEST**\n\n"
  SERENA += "**♡ My Creator :** [𝗧𝗨𝗦𝗛𝗔𝗥😍](t.me/Tushar204)\n\n"
  SERENA += "**♡ Telethon Version : 1.23.0**\n\n"
  BUTTON = [[Button.url("𝐒𝐔𝐏𝐏𝐎𝐑𝐓🙂", "https://t.me/LOVELYAPPEAL"), Button.url("𝐔𝐏𝐃𝐀𝐓𝐄", "https://t.me/LOVELY_ROBOTS")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=SERENA,  buttons=BUTTON)