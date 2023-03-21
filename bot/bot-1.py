#    Copyright (C) 2021 - Avishkar Patil | @AvishkarPatil


import os
import sys
import time
import logging
import pyrogram
import aiohttp
import asyncio
import requests
import aiofiles
import shutil
from random import randint
from progress import progress
from config import Config
import subprocess
import re
from pydub import AudioSegment
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, InputTextMessageContent
os.makedirs("input/temp",exist_ok=True)
os.makedirs("compressed/temp",exist_ok=True)
os.makedirs('decompressed',exist_ok=True)

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

DOWNLOAD = "./"

# vars
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN

   
bot = Client(
    "AnonFilesBot",
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)


START_TEXT = """
__Hᴇʟʟᴏ 😎 \n\n__This bot can compres and decompress audio using A.I__\n\n**
"""
HELP_TEXT = """
**send me a wav file and i will compress it and send u an ecdc file , also u culd send me an ecdc file and i will decompress it**
"""
ABOUT_TEXT = """
- **Bot :** `Sound compress`
- **Language :** [Python3](https://python.org)

__MᴀɪɴTᴀɪɴᴇᴅ Bʏ__ :** JPU 4TH PROJECT
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )


@bot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()
        
        
@bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

      
@bot.on_message(filters.media & filters.private)
async def upload(client, message):
    if Config.UPDATES_CHANNEL is not None:
        try:
            user = await client.get_chat_member(Config.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await client.send_message(
                    chat_id=message.chat.id,
                    text="**Sᴏʀʀʏ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ! Cᴏɴᴛᴀᴄᴛ** ",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await client.send_message(
                chat_id=message.chat.id,
                text="**🏃‍♂**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ ", url=f"https://t.me/{Config.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await client.send_message(
                chat_id=message.chat.id,
                text="**Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ! Cᴏɴᴛᴀᴄᴛ ᴍʏ** .",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    m = await message.reply("**Dᴏᴡɴʟᴏᴀᴅɪɴɢ the FIʟᴇs Tᴏ The Sᴇʀᴠᴇʀ ....** ")
    now = time.time()
    sed = await bot.download_media(
                message, DOWNLOAD,
          progress=progress,
          progress_args=(
            "**Uᴘʟᴏᴀᴅ Pʀᴏᴄᴇss Sᴛᴀʀᴇᴅ Wᴀɪᴛ ᴀɴᴅ Wᴀᴛᴄʜ Mᴀɢɪᴄ**\n**Iᴛs Tᴀᴋᴇ ᴛɪᴍᴇ Aᴄᴄᴏʀᴅɪɴɢ Yᴏᴜʀ Fɪʟᴇs Sɪᴢᴇ** \n\n**ᴇᴛᴀ:** ", 
            m,
            now
            )
        )
    try:
        files = {'file': open(sed, 'rb')}
        print(sed)
        ##with open("123.wav",'wb') as file:
            #file.write(files['file'])
        print("files file type",type(files['file']))
        #await m.edit("**Uᴘʟᴏᴀᴅɪɴɢ ᴛᴏ AɴᴏɴFIʟᴇs Sᴇʀᴠᴇʀ Pʟᴇᴀsᴇ Wᴀɪᴛ**")
        #callapi = requests.post("https://api.anonfiles.com/upload", files=files)
        """
        text = callapi.json()
        output = f
<u>**Fɪʟᴇ Uᴘʟᴏᴀᴅᴇᴅ Tᴏ AɴᴏɴFɪʟᴇs**</u>

**📂 Fɪʟᴇ Nᴀᴍᴇ:** {text['data']['file']['metadata']['name']}

**📦 Fɪʟᴇ Sɪᴢᴇ:** {text['data']['file']['metadata']['size']['readable']}

**📥Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ:** `{text['data']['file']['url']['full']}`

🔅"""
        #btn = InlineKeyboardMarkup(
            #                    [[InlineKeyboardButton("Dᴏᴡɴʟᴏᴀᴅ Fɪʟᴇ", url=f"{text['data']['file']['url']['full']}")]])
        #await m.edit(output, reply_markup=btn)
         
        file_name_temp=sed.split("/")[-1]
        sounds=['wav','ogg','mp3']
        if file_name_temp.split(".")[-1] in sounds:

            file_name_temp_sef=file_name_temp.split(".")[0]

            selfix=file_name_temp.split(".")[-1]

            names_1=re.sub('[^a-zA-Z1-9]+', '', file_name_temp_sef)
            names=names_1+"."+selfix
            shutil.copy(sed,'input/'+names)
            
            text=""""""
            text=text+f"""python -m encodec input/{names} compressed/{names_1}.ecdc -f
            """
            
            print("started compressing",text)
            ct=subprocess.call(text, shell=True,stderr=subprocess.STDOUT)
            if ct==1:
                await bot.send_message(message.chat.id,'This file is not supported for compression ')
                os.remove(sed)
                return 
            print('done compressing')
            await bot.send_audio(message.chat.id, f"compressed/{names_1}.ecdc")
        elif file_name_temp.split(".")[-1]=='ecdc':
            file_name_temp_sef=file_name_temp.split(".")[0]

            selfix=file_name_temp.split(".")[-1]

            names_1=re.sub('[^a-zA-Z1-9]+', '', file_name_temp_sef)
            names=names_1+"."+selfix
            file_name_temp_sef=file_name_temp.split(".")[0]
            shutil.copy(sed,'input/'+names)
            
            text=""""""
            text=text+f"""python -m encodec input/{names} decompressed/{names_1}.wav -f
            """
            
            print("started decompressing",text)
            ct=subprocess.call(text, shell=True,stderr=subprocess.STDOUT)
            if ct==1:
                await bot.send_message(message.chat.id,'This file is either not ecdc or coruapt  ')
                os.remove(sed)
                return 
            print('done decompressing')
            src = f"decompressed/{names_1}.wav"
            dst = f"decompressed/{names_1}.mp3"
            sound = AudioSegment.from_mp3(src)
            sound.export(dst, format="mp3")
            await bot.send_audio(message.chat.id, f"decompressed/{names_1}.mp3")
        else :
            await bot.send_message(message.chat.id,'This file is neither supported for compression or decompression')
            
        os.remove(sed)
        
    except Exception:
        await m.edit("__Pʀᴏᴄᴇss Fᴀɪʟᴇᴅ, Mᴀʏʙᴇ Tɪᴍᴇ Oᴜᴛ Dᴜᴇ Tᴏ Lᴀʀɢᴇ Fɪʟᴇ Sɪᴢᴇ!__")
        return
      
@bot.on_message(filters.regex(pattern="https://cdn-") & filters.private  )
async def url(client, message):
    msg = await message.reply("__Cʜᴇᴄᴋɪɴɢ Uʀʟ...__")
    lenk = message.text
    cap = "© @AvishkarPatil"
    thumb = "./thumb.jpg"
    try:
         await msg.edit("**Bɪɢ Fɪʟᴇs Wɪʟʟ Tᴀᴋᴇ Mᴏʀᴇ Tɪᴍᴇ, Dᴏɴ'ᴛ Pᴀɴɪᴄ!**")
         filename = await download(lenk)
         await msg.edit("Uploading File To Telegram...")
         await message.reply_document(filename, caption=cap, thumb=thumb)
         await msg.delete()
         os.remove(filename)
    except Exception:
        await msg.edit("__Pʀᴏᴄᴇss Fᴀɪʟᴇᴅ, Mᴀʏʙᴇ Tɪᴍᴇ Oᴜᴛ Dᴜᴇ Tᴏ Lᴀʀɢᴇ Fɪʟᴇ Sɪᴢᴇ!__")
        
async def download(url):
    ext = url.split(".")[-1]
    filename = str(randint(1000, 9999)) + "." + ext
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(filename, mode='wb')
                await f.write(await resp.read())
                await f.close()
    return filename
        
        
bot.start()
print("Bot Is Started!")
idle()
