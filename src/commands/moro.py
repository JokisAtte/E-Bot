import logging
from telegram import Update
from telegram.ext import (
    ContextTypes,
)
import auth
import database as db
import envreader

#käytetään ekaan kirjautumiseen.
async def moro_callback(update: Update, context) -> None:
    if(auth.authenticate_user(update.effective_user.id)):
        msg = 'Ollaan jo moroteltu @%s. Voit käyttää muita komentojani yksityisviesteinä!' % (update.effective_user.username)
    else:
        id = str(update.effective_chat.id)
        msg = 'Väärä ryhmä'
        print("id:", type(id), id)
        print("envreader.get_var(GROUP_TEST):", type(envreader.get_var("GROUP_TEST")), envreader.get_var("GROUP_TEST"))
        #Tarkista onko viesti lähetetty E tai aktiivicase ryhmässä
        if(id == envreader.get_var("GROUP_ID_AKTIIVICASE") or id == envreader.get_var("GROUP_ID_E") or id == envreader.get_var("GROUP_TEST")):
            #Lisää käyttäjä kantaan, tarkisa menikö se läpi
            if(len(str(db.new_user(update.effective_user)))>0):
                msg = 'Käyttäjä @%s lisätty. Anna käskyt jatkossa yksityisviestinä.' % (update.effective_user.username)
            else:
                msg = 'Joku ongelma, pingaa ylläpitoa :D'

    await update.message.reply_text(msg)
