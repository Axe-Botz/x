from pyrogram import filters, Client
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message

IMG = ""

@Client.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{IMG}",
        caption="👋 Hello, I'm Alive.",
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
    buttons =
    med = InputMediaPhoto(
        media="https://telegra.ph//file/6f7d35131f69951c74ee5.jpg"        
    )
    await CallbackQuery.edit_message_media(media=med)
