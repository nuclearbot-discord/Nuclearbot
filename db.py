#''' # - Эта хрень нужна мне не удаляй *

from firebase import Firebase

configfb = {
  "apiKey": "AIzaSyC3vGWkRWrBNLuz5YlysXZMZXGy0gT56LA",
  "authDomain": "164893195950.firebaseapp.com",
  "databaseURL": "https://avroraacha.firebaseio.com/",
  "storageBucket": "avroraacha.appspot.com" 
}

firebase = Firebase (configfb)
db = firebase.database ()

def db_setchance (chance, guild_id):
    data = {"shans": chance}
    db.child ("timeout").child (guild_id).set (data)

def db_getchance (guild_id):
    all_users = db.child ("timeout").get ()

    for user in all_users.each ():
        kkey = user.key ()
        
        if str (kkey) == str (guild_id):    
            a = user.val ()
            return a ["shans"]
def dbmcget():
    all_acc1 = db.child("accs").get()
    accs2=[]
    for user in all_acc1.each():
        accs2.append(user.key()+":"+user.val())
    rnd=random.choice(accs2)
    accitog=rnd.split(":")
    return str(accitog[1])+"- пароль\n"+str(accitog[0])+"- почта"
def add_minecraft(email, pass):
  db.child("accs").child (email).set (pass)
'''
def adm_give(id):
  #give id of admin:
  adms = db.child("adms").get()
  for iamadmin in adms.each ():
      kkeyadm = iamadmin.key ()
        
      if str (kkeyadm) == str (id):    
          return True
      else:
          return False'''
         
''' # Смотри *

def db_setchance (a, b):
    pass

def db_getchance (a):
    return '50'

#'''# Смотри *
