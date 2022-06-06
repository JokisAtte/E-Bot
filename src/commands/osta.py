import logging
from telegram import (Update, ReplyKeyboardMarkup)
from telegram.ext import (
    ContextTypes,
)
import auth
import database as db

async def osta_callback(update: Update, context) -> None:
    if(auth.authenticate_user(update.effective_user.id) == False):
        msg = "Joko olet väärässä paikassa tai et ole ottanut bottia käyttöön oikein 🕶️"
    else:
        amount = update.message.text.split(" ")
        print(amount)
        #näytä rivi nappeja
        kb = ReplyKeyboardMarkup([["1","1.5","2"],["2.5","3","Muu summa"]], one_time_keyboard=True, resize_keyboard=True)
        asd = await update.message.reply_text("Valitse piikille lisättävä summa", reply_markup=kb)
        print("ASDASD")
        print(asd.text)
        #db.new_purchase(update.effective_user.id, amount)
        msg = "Piikki lisätty. Piikkisi nyt on %s €" % (10000000)
    await update.message.reply_text(msg)
