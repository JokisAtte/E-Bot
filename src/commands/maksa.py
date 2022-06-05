import logging
from telegram import Update
from telegram.ext import (
    CallbackContext,
    ContextTypes,
)

async def maksa_callback(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    
    msg = (
        "placeholder"
    )

    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)