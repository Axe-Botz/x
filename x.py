import asyncio
import os

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery


IMG = ""

def get_image(videoid, user_id):
    if os.path.isfile(f"cache/{videoid}_{user_id}.png"):
        return f"cache/{videoid}_{user_id}.png"
    else:
        return f"{IMG}"

  ## ---------------------------------------------------- ##

