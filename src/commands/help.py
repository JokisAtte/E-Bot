import logging
from telegram import Update
from telegram.ext import (
    ContextTypes,
)
import auth

async def help_callback(update: Update, context) -> None:
    #Jos komento annettu ryhmässä
    chat_id = str(update.effective_chat.id)
    user_id = str(update.effective_user.id)
    if(auth.message_is_from_correct_group(chat_id)):
        msg = "Hei! Olen kerhon piikkibotti.\n Rekisteröidy käyttäjäksi lähettämällä tässä ryhmässä /moro. Rekisteröityminen täytyy tehdä vain kerran. \n Muita komentoja käytetään yksityisviesteinä."
    elif(auth.authenticate_user(update.effective_user.id)):
        #listaa komennot
        commands = ['/moro - Rekisteröidy käyttäjäksi. Tämä täytyy tehdä vain kerran', '/osta - osta tuote haluamallasi summalla. Esimerkiksi \"/osta 2\" lisää 2 € piikille', '/piikki - Tarkista nykyinen piikkisi', '/maksa - Maksa piikkiä pois haluamallasi summalla. Esimerkiksi \"/maksa 10\" maksaa 10 € piikkiä pois', '/help - Listaa komennot']
        msg = "Komennot:\n"
        for command in commands:
            msg += command + "\n"

    await update.message.reply_text(msg)