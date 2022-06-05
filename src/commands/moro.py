import logging
from telegram import Update
from telegram.ext import (
    ContextTypes,
    CallbackContext
)

async def moro_callback(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    
    userid = update.effective_user.id
    
    # Auth failed ->
    if(userid==0): return
    
    
    
    # Auth ok ->
    msg = (
        "Tervetuloa käyttämään piikkiä!"
    )

    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)