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
