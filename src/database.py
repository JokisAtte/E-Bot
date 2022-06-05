from pymongo import MongoClient
import pymongo
import envreader
import datetime

client = MongoClient(envreader.get_var("MONGO_DB_URI"))

db = client["users"]

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
    'payments':{
        "type": payment_schema
    }
}
# Lisää uuden käyttäjän kantaan
# user_id: Telegramin käyttäjän id string
# return: Käyttäjän _id
def new_user(user_id):
    user = {
        'handle': "TODO",
        "tg_id": user_id,
        "balance": 0,
        "payments": []
    }
    return db.users.insert_one(user).inserted_id

#Etsii yhden käyttäjän
#user_id: Telegramin käyttäjän id string
#return: Käyttäjän tiedot
def find_user(user_id):
    return db.users.find_one({"tg_id":user_id})

#Lisää käyttäjälle uuden maksun (eli piikkiä ostettu)
#user_id: Telegramin käyttäjän id string
#amount: Maksun määrä
#return: Boolean menikö maksu läpi onnistuneesti
def new_payment(user_id, maksu):
    user = find_user(user_id)
    if(user == None):
        return False
    payment_obj = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "amount": maksu
    }
    user["payments"].append(payment_obj)
    user["balance"] += maksu
    return bool(db.users.update_one({"tg_id":user_id}, {"$set": user}).modified_count)

#Etsii kaikki käyttjät
#return: lista kaikista käyttäjistä
def get_users():
    return list(db.users.find())

#Lisää uuden ostoksen käyttäjälle
#user_id: Telegramin käyttäjän id string
#amount: Ostoksen määrä
#return: Boolean menikö maksu läpi onnistuneesti
def new_purchase(user_id, amount):
    user = find_user(user_id)
    if(user == None):
        return False
    user["balance"] += amount   
    return bool(db.users.update_one({"tg_id":user_id}, {"$set": user}).modified_count)