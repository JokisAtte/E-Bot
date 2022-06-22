import logging
from telegram import (Update, ReplyKeyboardMarkup, KeyboardButton )
from telegram.ext import (
    ContextTypes,

)
import auth
import database as db

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

async def osta_callback(update: Update, context) -> None:
    if(auth.authenticate_user(update.effective_user.id) == False):
        return await update.message.reply_text("Joko olet väärässä paikassa tai et ole ottanut bottia käyttöön oikein 🕶️")
    if(auth.message_is_from_correct_group(update.effective_chat)):
        return await update.message.reply_text("Käytä komentoa /osta vain yksityisviestillä")

    msg = update.message.text.split(" ")
    if(len(msg)==1): #jos annettu vain /osta, näytetään valikko mistä valitaan summa
        amounts = [1, 1.5, 2, 2.5, 3]
        kb = ReplyKeyboardMarkup.from_column([KeyboardButton('/osta {} €'.format(i)) for i in amounts], one_time_keyboard=True)
        await update.message.reply_text(text="Valitse summa tai käytä komentoa \"/osta <summa>\". esim \"/osta 1\"" , reply_markup=kb)
    elif(len(msg)>1): #Jos annettu myös summa lisätään summa piikkiin
        amount = msg[1].strip('€eE')
        if(is_float(amount) and float(amount)>0):
            result = db.new_purchase(update.effective_user.id, -1 * float(amount))
            if(result != None):
                await update.message.reply_text("Maksu lisätty. Tämänhetkinen saldo: {} €".format(result["balance"]))
        else: #jos ei ole, hauku käyttäjää
            await update.message.reply_text("Tarkista komento. Esimerkki: /osta 2")