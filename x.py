from pyrogram import filters, Client
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message, InputMediaVideo

IMG = ""
TEXT = "👋 Hello, I'm Alive."
@Client.on_message(filters.command("start"))
async def start(client: Client, message: Message):
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
        


@Client.on_callback_query(filters.regex("zeno"))
async def queued_tracks(client, CallbackQuery: CallbackQuery, _):
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
    await CallbackQuery.edit_message_media(media=med)


@Client.on_callback_query(filters.regex("start"))
async def queued_tracks(client, CallbackQuery: CallbackQuery, _):
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

