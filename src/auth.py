import database as db
import telegram

def authenticate_user(user_id):
    if(db.find_user(user_id) != None):
        return True
    else:
        print(telegram.getChatMember(user_id, -1471217097))
        print(telegram.getChatMember(user_id, -1123629842))
print(authenticate_user("33333"))
#hae henkilö kannasta

#jos on niin palauta true

#jos ei:
    #tarkista onko henkilö E ryhmässä tai aktiivicasessa

    #jos ei niin palauta false

    #jos on niin lisää kantaan

    #palauta true