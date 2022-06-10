import logging
from tokenize import Token
from telegram import Update
from telegram.ext import Updater, ApplicationBuilder, CallbackContext, CommandHandler, CallbackQueryHandler, ContextTypes

import envreader

from commands.maksa import maksa_callback
from commands.osta import osta_callback
from commands.moro import moro_callback

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    TOKEN = envreader.get_var('TOKEN')
    application = ApplicationBuilder().token(TOKEN).arbitrary_callback_data(True).build()
    
    handlers = [CommandHandler('moro', moro_callback),
                CommandHandler('osta', osta_callback),
                CommandHandler('maksa', maksa_callback)
                ]
    
    for handler in handlers:
        application.add_handler(handler)
    
    application.run_polling()
