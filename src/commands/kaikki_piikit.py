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

async def kaikki_piikit_callback(update: Update, context) -> None:
    msg = "Virhe autentikoinnissa. Oletko sanonut /moro ryhmässä?"
    if(auth.authenticate_user(update.effective_user.id)):
        users = db.get_all_users()
        result = []
        msg = ""
        for i in users:
            result.append({'handle': i['handle'], 'balance': i['balance']})
        result_sorted = sorted(result, key=lambda k: k['balance'])
        for i in result_sorted:
            msg += '{}: {} € \n'.format(i['handle'], i['balance'])
    await update.message.reply_text(msg) 