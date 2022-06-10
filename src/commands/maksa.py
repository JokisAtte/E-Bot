import logging
from telegram import Update
from telegram.ext import (
    ContextTypes,
)
import auth
import database as db

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

async def maksa_callback(update: Update, context) -> None:
    if(auth.authenticate_user(update.effective_user.id) == False):
        await update.message.reply_text("Joko olet väärässä paikassa tai et ole ottanut bottia käyttöön oikein 🕶️")
        return

    msg = update.message.text.split(" ")
    if(len(msg)==1): #jos annettu vain /maksa, pyydetään antamaan summa maksukomennossa
        await update.message.reply_text(text="Anna maksun summa. Esimerkki: /maksa 100")
    else: #Lisää maksu kantaan, päivitä piikin saldo
        amount = msg[1]
        if(is_float(amount)):
            user_id = update.effective_user.id
            user = db.find_user(user_id)
            if(user != None):
                if(db.new_payment(user["tg_id"], float(amount))):
                    await update.message.reply_text("Maksu lisätty. Tämänhetkinen saldo: {} €".format(user["balance"]))
                else:
                    await update.message.reply_text("Jokin ongelma, pingaa ylläpitoa :D")
        else:
            await update.message.reply_text("Tarkista komento. Esimerkki: /maksa 100")
