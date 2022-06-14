import logging
from telegram import Update
from telegram.ext import (
    ContextTypes,
)
import auth
import database as db
import envreader

#Hae käyttäj
async def piikki_callback(update: Update, context) -> None:
    msg = "Virhe autentikoinnissa. Oletko sanonut /moro ryhmässä?"
    if(auth.authenticate_user(update.effective_user.id)):
        balance = db.find_user(update.effective_user.id)['balance']
        msg = 'Piikkisi on {} €'.format(balance)
        
    await update.message.reply_text(msg) 