import logging
from telegram import (Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, CallbackQuery, )
from telegram.ext import (
    ContextTypes,
    CallbackQueryHandler,
    
)
import auth
import database as db

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

async def osta_callback(update: Update, context) -> None:
    if(auth.authenticate_user(update.effective_user.id) == False):
        await update.message.reply_text("Joko olet väärässä paikassa tai et ole ottanut bottia käyttöön oikein 🕶️")
        return
    
    msg = update.message.text.split(" ")
    if(len(msg)==1): #jos annettu vain /osta, näytetään valikko mistä valitaan summa
        amounts = [1, 1.5, 2, 2.5, 3]
        kb = ReplyKeyboardMarkup.from_column([KeyboardButton('/osta {} €'.format(i)) for i in amounts], one_time_keyboard=True)
        await update.message.reply_text(text="Valitse summa tai käytä komentoa \"/osta <summa>\". esim \"/osta 1\"" , reply_markup=kb)
    elif(len(msg)>1): #Jos annettu myös summa lisätään summa piikkiin
        amount = msg[1]
        if(is_float(amount)):
            user_id = update.effective_user.id
            user = db.find_user(user_id)
            if(user != None):
                db.new_purchase(user["tg_id"], -1 * float(amount))
                await update.message.reply_text("Maksu lisätty. Tämänhetkinen saldo: {} €".format(user["balance"]))
        else: #jos ei ole, hauku käyttäjää
            await update.message.reply_text("Tarkista komento. Esimerkki: /osta 2")