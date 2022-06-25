from pymongo import MongoClient, ReturnDocument
import pymongo
import envreader
import datetime
import logging

client = MongoClient(envreader.get_var("MONGO_DB_URI"))

db = client["users"]

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

payment_schema = {
    'date': {
        "type": str,
        "required": True
    },
    'amount': {
        "type": str,
        "required": True
    }
}

user_schema = {
    'handle': {
        "type": str,
        "required": True
    },
    'tg_id': {
        "type": str,
        "required": True
    },
    'balance': {
        "type": int,
        "required": True
    },
    'history':{
        "type": payment_schema
    }
}

# Lisää uuden käyttäjän kantaan
# user_id: Telegramin käyttäjä. Tyyppi: telegram.User
# return: Käyttäjän _id string, tyhjä string jos virhe
def new_user(user):
    newUser = {
        'handle': user.username,
        "tg_id": user.id,
        "balance": 0,
        "history": []
    }
    try:
        return db.users.insert_one(newUser).inserted_id
    except:
        print("virhe tietokannassa")
        return ""

#Etsii yhden käyttäjän
#user_id: Telegramin käyttäjän id string
#return: Käyttäjän tiedot
def find_user(user_id):
    return db.users.find_one({"tg_id":user_id})

#Lisää käyttäjälle uuden maksun (eli piikkiä ostettu)
#user_id: Telegramin käyttäjän id string
#amount: Maksun määrä
#return: Päivitetty dokumentti tai None jos virhe
def new_payment(user_id, amount):
    user = find_user(user_id)
    if(user == None):
        return False
    payment_obj = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "amount": amount
    }
    user["history"].append(payment_obj)
    user["balance"] += amount
    return db.users.find_one_and_update({"tg_id":user_id}, {"$set": user}, return_document=ReturnDocument.AFTER, upsert=True)

#Etsii kaikki käyttjät
#return: lista kaikista käyttäjistä
def get_all_users():
    return list(db.users.find())

#Lisää uuden ostoksen käyttäjälle
#user_id: Telegramin käyttäjän id string
#amount: Ostoksen määrä
#return: Päivitetty dokumentti tai None jos virhe
def new_purchase(user_id, amount):
    user = find_user(user_id)
    if(user == None):
        return False
    payment_obj = {
    "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "amount": amount
    }
    user["history"].append(payment_obj)
    user["balance"] += amount   
    return db.users.find_one_and_update({"tg_id":user_id}, {"$set": user}, return_document=ReturnDocument.AFTER, upsert=True)