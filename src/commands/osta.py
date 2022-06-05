import logging
from telegram import Update
from telegram.ext import (
    ContextTypes,
    CallbackContext
)

async def osta_callback(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    
    msg = (
        "placeholder"
    )

    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
