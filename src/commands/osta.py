import logging
from telegram import (Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, CallbackQuery, )
from telegram.ext import (
    ContextTypes,
    CallbackQueryHandler,
    
)
import auth
import database as db

def is_float(element) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False

async def osta_callback(update: Update, context) -> None:
    msg = update.message.text.split(" ")
    amounts = [1, 1.5, 2, 2.5, 3]
    if(auth.authenticate_user(update.effective_user.id) == False):
        await update.message.reply_text("Joko olet väärässä paikassa tai et ole ottanut bottia käyttöön oikein 🕶️")
        return

    if(len(msg)==1): #jos annettu vain /osta, näytetään valikko mistä valitaan summa
        kb = ReplyKeyboardMarkup.from_column([KeyboardButton('/osta {} €'.format(i)) for i in amounts], one_time_keyboard=True)
        await update.message.reply_text(text="Valitse summa. Jos haluat muun summan, käytä /osta <summa>. esim /osta 1" , reply_markup=kb)
    elif(len(msg)>1): #Jos annettu myös summa lisätään summa piikkiin
        amount = msg[1]
        #if(is_int(amount) | is_float(amount)): #tarkista että summa on sopiva numero
        if(is_float(amount)):
            #Add the amount to the database for user
            user_id = update.effective_user.id
            user = db.find_user(user_id)
            if(user != None):
                db.new_purchase(user["tg_id"], -1 * float(amount))
                await update.message.reply_text("Tili done")
        else: #jos ei ole hauku käyttäjää
            await update.message.reply_text("Tarkista komento. Esimerkki: /osta 2")