import logging
from telegram import Update
from telegram.ext import (
    ContextTypes,
)

async def maksa_callback(update: Update) -> None:
    
    msg = (
        "placeholder"
    )

    await update.message.reply_text(msg)
