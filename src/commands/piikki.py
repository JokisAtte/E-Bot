import logging
from telegram import Update
from telegram.ext import (
    ContextTypes,
)
import auth
import database as db
import envreader

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#Hae käyttäj
async def piikki_callback(update: Update, context) -> None:
    msg = "Virhe autentikoinnissa. Oletko sanonut /moro ryhmässä?"
    
    if(auth.authenticate_user(update.effective_user.id)):
        if(auth.message_is_from_correct_group(update.effective_chat.id)):
            return await update.message.reply_text("Käytä komentoa /piikki vain yksityisviestillä")
        
        balance = db.find_user(update.effective_user.id)['balance']
        msg = 'Piikkisi on {} €'.format(balance)
        
    return await update.message.reply_text(msg) 