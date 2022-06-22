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

#käytetään ekaan kirjautumiseen.
async def moro_callback(update: Update, context) -> None:
    if(auth.authenticate_user(update.effective_user.id)):
        msg = 'Ollaan jo moroteltu @%s. Voit käyttää muita komentojani yksityisviesteinä!' % (update.effective_user.username)
    else:
        id = str(update.effective_chat.id)
        msg = 'Väärä ryhmä'
        #Tarkista onko viesti lähetetty E tai aktiivicase ryhmässä
        if(auth.message_is_from_correct_group(update.effective_chat)):
            #Lisää käyttäjä kantaan, tarkisa menikö se läpi
            if(len(str(db.new_user(update.effective_user)))>0):
                msg = 'Käyttäjä @%s lisätty. Anna käskyt jatkossa yksityisviestinä.' % (update.effective_user.username)
            else:
                msg = 'Joku ongelma, pingaa ylläpitoa :D'

    await update.message.reply_text(msg)
