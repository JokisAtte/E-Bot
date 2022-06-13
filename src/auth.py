import database as db
import telegram
import envreader

def authenticate_user(user_id):
    user = db.find_user(user_id)
    if(user != None):
        return True
    else:
        return False

def message_is_from_correct_group(group_id):
    return group_id == envreader.get_var("GROUP_ID_E") or group_id == envreader.get_var("GROUP_TEST") or  group_id == envreader.get_var("GROUP_ID_AKTIIVICASE")