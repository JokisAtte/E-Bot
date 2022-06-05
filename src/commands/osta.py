import logging
from telegram import Update
from telegram.ext import (
    ContextTypes,
)

async def osta_callback(update: Update) -> None:
    
    msg = (
        "placeholder"
    )

    await update.message.reply_text(msg)
