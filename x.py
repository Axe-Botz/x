import asyncio
import os

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton

API_ID = 'YOUR_API_ID'
API_HASH = 'YOUR_API_HASH'
BOT_TOKEN = 'YOUR_BOT_TOKEN'

app = Client("video_button_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


IMG = ""

def get_image(videoid, user_id):
    if os.path.isfile(f"cache/{videoid}_{user_id}.png"):
        return f"cache/{videoid}_{user_id}.png"
    else:
        return f"{IMG}"

  ## ---------------------------------------------------- ##


@app.on_callback_query(filters.regex("zeno"))
async def queued_tracks(client, CallbackQuery: CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    med = InputMediaPhoto(
        media="https://telegra.ph//file/6f7d35131f69951c74ee5.jpg",
        caption="Hello, Testing!",
    )
    await CallbackQuery.edit_message_media(media=med)


# Function to send the video with the back button
def send_video_with_back_button(chat_id, video_file_id, original_message_id):
    back_button = InlineKeyboardButton("Back", callback_data=f"back:{original_message_id}")
    markup = InlineKeyboardMarkup([[back_button]])
    app.send_video(chat_id, video_file_id, reply_markup=markup)

# Function to send the original message with the video button
def send_original_message_with_button(chat_id, original_message):
    video_button = InlineKeyboardButton("Watch Video", callback_data=f"video:{original_message.message_id}")
    markup = InlineKeyboardMarkup([[video_button]])
    app.send_message(chat_id, original_message.text, reply_markup=markup)

# Handle callback queries
@app.on_callback_query()
def handle_callback(bot, query: CallbackQuery):
    data = query.data.split(":")
    action = data[0]
    original_message_id = int(data[1])

    if action == "video":
        # Replace this with the actual video file ID
        video_file_id = "YOUR_VIDEO_FILE_ID"
        send_video_with_back_button(query.message.chat.id, video_file_id, original_message_id)
        bot.answer_callback_query(query.id)

    elif action == "back":
        original_message = app.get_messages(query.message.chat.id, message_ids=original_message_id)
        send_original_message_with_button(query.message.chat.id, original_message)
        bot.answer_callback_query(query.id)

# Start the bot
app.run()
