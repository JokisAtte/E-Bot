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
    #autentikoi

    #näytä grid
    grid = telegram.reply_keyboard_markup([["1 €","1.5 €","2 €"],["2.5 €","3 €","Muu summa"]],one_time_keyboard = True, resize_keyboard = True)
    update.message.reply_text(msg, reply_markup = grid)
    #kirjaa kantaan

    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
