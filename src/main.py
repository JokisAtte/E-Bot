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

def kb_callback(update, context):
    print("jojoasjdaosjdoasd")
    query = update.callback_query
    print(query.data)
    query.answer()

async def list_button(update: Update, context: ContextTypes) -> None:
    """Parses the CallbackQuery and updates the message text."""
    print("AAAAAAAAA")
    query = update.callback_query
    await query.answer()
    # Get the data from the callback_data.
    # If you're using a type checker like MyPy, you'll have to use typing.cast
    # to make the checker get the expected type of the callback_data
    #number, number_list = cast(Tuple[int, List[int]], query.data)
    # append the number to the list
    #number_list.append(number)

    #await query.edit_message_text(
    #    text=f"So far you've selected {number_list}. Choose the next item:",
    #    reply_markup=build_keyboard(number_list),
    #)
    print(query)
    # we can delete the data stored for the query, because we've replaced the buttons
    context.drop_callback_data(query)

if __name__ == '__main__':
    TOKEN = envreader.get_var('TOKEN')
    application = ApplicationBuilder().token(TOKEN).arbitrary_callback_data(True).build()
    
    handlers = [CommandHandler('moro', moro_callback),
                CommandHandler('osta', osta_callback),
                CommandHandler('maksa', maksa_callback)
                ]
    
    for handler in handlers:
        application.add_handler(handler)
    #update = Update(1, use_context = True)
    application.add_handler(CallbackQueryHandler(list_button))
    
    application.run_polling()
