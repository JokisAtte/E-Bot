import logging
from telegram import (Update, ReplyKeyboardMarkup, KeyboardButton )
from telegram.ext import (
    ContextTypes,
)
import auth
import database as db
import envreader as env

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

async def laheta_viesti_maksusta(update, user, amount):
    return await update.message.reply_text("{user} maksoi {amount} €", chat_id = env.get_var('GROUP_TEST'))

async def maksa_callback(update: Update, context) -> None:
    if(auth.authenticate_user(update.effective_user.id) == False):
        return await update.message.reply_text("Joko olet väärässä paikassa tai et ole ottanut bottia käyttöön oikein 🕶️")
    if(auth.message_is_from_correct_group(update.effective_chat.id)):
        return await update.message.reply_text("Käytä komentoa /maksa vain yksityisviestillä")

    msg = update.message.text.split(" ")
    if(len(msg)==1): #jos annettu vain /maksa, pyydetään antamaan summa maksukomennossa
        amounts = [5, 10, 15, 20, 50]
        kb = ReplyKeyboardMarkup.from_column([KeyboardButton('/maksa {} €'.format(i)) for i in amounts], one_time_keyboard=True)
        await update.message.reply_text(text="Valitse summa tai käytä komentoa \"/maksa <summa>\". esim \"/maksa 1\"" , reply_markup=kb)
    else: #Lisää maksu kantaan, päivitä piikin saldo
        amount = msg[1].strip('€eE')
        if(is_float(amount) and float(amount)>0): #Pitää olla luku ja yli 0
            user_id = update.effective_user.id
            user = db.find_user(user_id)
            if(user != None): #Käyttäjä pitää löytyä
                result = db.new_payment(user["tg_id"], float(amount))
                if(result != None): #Päivitys onnistui
                    await laheta_viesti_maksusta(update, user_id, amount)
                    await update.message.reply_text("Maksu lisätty. Tämänhetkinen saldo: {} €".format(result["balance"]))
                else:
                    await update.message.reply_text("Jokin ongelma, pingaa ylläpitoa :D")
        else:
            await update.message.reply_text("Tarkista komento. Esimerkki: /maksa 100")
