import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler



async def moro_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    # Autentikointi ->
   
    
    msg = (
        ""
    )

    await update.message.reply_text(msg)
