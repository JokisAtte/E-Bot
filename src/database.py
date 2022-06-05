from pymongo import MongoClient
import pymongo
import envreader
import datetime

client = MongoClient(envreader.get_var("MONGO_DB_URI"))

db = client["users"]

payment_schema = {
    'date': {
        type: type(datetime.date()),
        required: True
    },
    'amount': {
        type: int,
        required: True
    }
}

user_schema = {
    'handle': {
        type: str,
        "required": True
    },
    'tg_id': {
        type: str,
        "required": True
    },
    'balance': {
        type: int,
        "required": True
    },
    'payments':{
        type: payment_schema
    }
}



def new_user(user_id):
    print("todo")

def find_user(user_id):
    return db.users.find_one({"user_id":user_id})

def save_payment(maksu):
    print("todo")

def get_users():
    return db.users.find()

def new_purchase(user_id, amount):
    print("todo")