import logging
from telegram import (Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, CallbackQuery)
from telegram.ext import (
    ContextTypes,
    CallbackQueryHandler
)
import auth
import database as db

async def osta_callback(update: Update, context) -> None:
    if(auth.authenticate_user(update.effective_user.id) == False):
        msg = "Joko olet väärässä paikassa tai et ole ottanut bottia käyttöön oikein 🕶️"
    else:
        amount = update.message.text.split(" ")

#       summat = [["1","1.5","2"],["2.5","3","Muu summa"]]
#        napit1 = []
#        napit2 = []
#        for i in summat[0]:
#             napit1.append(InlineKeyboardButton(i,callback_data=i[0]))
#        for i in summat[1]:
##            napit2.append(InlineKeyboardButton(i,callback_data=i[0]))
##        napit = [napit1,napit2]
#        reply_markup = ReplyKeyboardMarkup(napit)
#        Bot.send_message(text = "Valitse summa:", reply_markup=reply_markup)
        #näytä rivi nappeja
        kb = InlineKeyboardMarkup(inline_keyboard= [[InlineKeyboardButton(text = "FFF", callback_data = (1, 1)), InlineKeyboardButton(text = "AAA", callback_data = (2, 2))]], one_time_keyboard=True, resize_keyboard=True)
        await update.message.reply_text(text="123123" , reply_markup=kb)
        #db.new_purchase(update.effective_user.id, amount)
        msg = "Piikki lisätty. Piikkisi nyt on %s €" % (10000000)
    #await update.message.reply_text(msg)
