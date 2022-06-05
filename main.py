import logging
from tokenize import Token
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler

import envreader

from .commands.maksa import maksa_callback
from .commands.osta import osta_callback
from .commands.moro import moro_callback

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

if __name__ == '__main__':
    TOKEN = envreader.get_var('TOKEN')
    application = ApplicationBuilder().token(TOKEN).build()
    
    handlers = [CommandHandler('start', start),
                CommandHandler('start', moro_callback),
                CommandHandler('start', osta_callback),
                CommandHandler('start', maksa_callback)]
    
    for handler in handlers:
        application.add_handler(handler)
    
    application.run_polling()
