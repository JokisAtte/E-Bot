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

def new_user(user_id):
    user = {
        'handle': "TODO",
        "tg_id": user_id,
        "balance": 0,
        "payments": []
    }
    return db.users.insert_one(user)

def find_user(user_id):
    return db.users.find_one({"tg_id":user_id})

def new_payment(user_id, maksu):
    user = find_user(user_id)
    payment_obj = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "amount": maksu
    }
    user["payments"].append(payment_obj)
    user["balance"] += maksu
    db.users.update_one({"tg_id":user_id}, {"$set": user})

def get_users():
    return list(db.users.find())

def new_purchase(user_id, amount):
    user = find_user(user_id)
    user["balance"] += amount   
    return db.users.update_one({"tg_id":user_id}, {"$set": user})