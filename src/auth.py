import database as db
import telegram

def authenticate_user(user_id):
    user = db.find_user(user_id)
    print(user)
    if(user != None):
        return True
    else:
        return False