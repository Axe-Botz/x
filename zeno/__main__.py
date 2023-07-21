
import asyncio

from pyrogram import filters, Client, idle
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message, InputMediaVideo, InlineKeyboardButton, InlineKeyboardMarkup

API_ID = 7839236
API_HASH = "5c34945e1a52089f3bf434a44b25aa1d"
TOKEN = "6122610087:AAG0Gox3EOyjfHvpsNsCyuTEm-IZiB9uygE"

bot = Client(
    "Client",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
)
## ---------------------------------------------------- ##

IMG = "https://te.legra.ph/file/c8de202c68588828a9250.jpg"
TEXT = "👋 Hello, I'm Alive."

@bot.on_message(filters.command("start"))
async def start(bot: Client, message: Message):
    await message.reply_photo(
        photo=f"{IMG}",
        caption=TEXT,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Working?", callback_data="zeno")
                ]
           ]
        ),
    )        
        


@bot.on_callback_query(filters.regex("zeno"))
async def queuedracks(bot, CallbackQuery: CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    await CallbackQuery.answer()
    buttons = [
            [
                InlineKeyboardButton("Back?", callback_data="start")
            ]
    ]
    med = InputMediaVideo(
        media="https://te.legra.ph/file/f19d43253efd0a4409132.mp4"        
    )
    await CallbackQuery.edit_message_media(
        media=med, reply_markup=buttons
    )


@bot.on_callback_query(filters.regex("start"))
async def queued(bot, CallbackQuery: CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    await CallbackQuery.answer()
    upl = [
            [
                InlineKeyboardButton("Working?", callback_data="zeno")
            ]
                ]    
    med = InputMediaPhoto(media=IMG, caption=TEXT)
    await CallbackQuery.edit_message_media(
        media=med, reply_markup=upl
    )

bot.start()
print("Bot Started!")

if __name__ == "__main__":
  #loop.run_until_complete(start_bot())
  idle()
