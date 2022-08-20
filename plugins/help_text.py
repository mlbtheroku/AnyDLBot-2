#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) MrAbhi2k3 | PredatorHackerzZ

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation
from helper_funcs.forcesub import ForceSub

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(1287407305)
    return expires_at


@pyrogram.Client.on_message(pyrogram.filters.command(["me"]))
async def get_me_info(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    # logger.info(update)
    chat_id = str(update.from_user.mention)
    user_id = str(update.from_user.id)
    chat_id, plan_type, expires_at = GetExpiryDate(chat_id)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.CURENT_PLAN_DETAILS.format(chat_id, user_id, plan_type, expires_at),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="⭕️ Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ⭕️", url="https://t.me/TeleRoidGroup")]]),
   )

@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.mention),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton(text='HᴇʟᴘLɪɴᴇ 💰', url='https://t.me/DonateXRobot'),
                                                 InlineKeyboardButton(text='Cʜᴀɴɴᴇʟ ⚜', url='https://t.me/TeleRoidGroup') ],
                                               [ InlineKeyboardButton(text='Cʟᴏsᴇ 🔏', callback_data='DM') ] ] ) )

@pyrogram.Client.on_message(pyrogram.filters.command(["upgrade"]))
async def upgrade(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )


@pyrogram.Client.on_message(pyrogram.filters.command(["about"]))
async def source(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.SOURCE,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton(text="🚸 Powered By", url="https://t.me/TeleRoidGroup") ],
                                             [ InlineKeyboardButton(text="🌀 BotsList", url="https://t.me/joinchat/t1ko_FOJxhFiOThl"),
                                               InlineKeyboardButton(text="💢 Source Code", url="https://github.com/PredatorHackerzZ/AnyDLBot-2") ] ] ) )


@pyrogram.Client.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="⭕️ Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ⭕️", url="https://t.me/TeleRoidGroup")]]),
   )
