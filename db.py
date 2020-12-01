#''' # - Эта хрень нужна мне не удаляй *
import os
import random
from random import Random

from firebase import Firebase

from config import settings

keyfb = os.environ ["KEY"]
chifrifb = os.environ ["KEYCF"]

configfb = {
    "apiKey": keyfb,
    "authDomain": chifrifb + ".firebaseapp.com",
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
def onjn(guild2):
    data = {
        "shans": "20",
        "lang":"eng"
    }
    db.child("timeout").child(guild2.id).set(data)
    
def dbmcget():
    all_acc1 = db.child("accs").get()
    accs2=[]
    for user in all_acc1.each():
        accs2.append(user.key()+":"+user.val())
    rnd=random.choice(accs2)
    accitog=rnd.split(":")
    return [str(accitog[0]), str(accitog[1])]

def add_minecraft(email, passw):
    db.child("accs").child (email).set (passw)
  
def adm_give(id_):
    admins_list = []
    
    adms = db.child("adms").get()
    for iamadmin in adms.each ():
        amins_list.append (str (iamadmin.key ()))

    return str (id_) in admins_list
        
''' # Смотри *

def db_setchance (a, b):
    pass

def db_getchance (a):
    return '20'

def onjn (a):
    pass

def dbmcget ():
    return ['ppap@ppap.ppap', 'ppap???']

def add_minecraft (a, b):
    pass

def adm_give (id_):
    return True

#'''# Смотри *

__all__ = ['db_setchance', 'db_getchance', 'onjn', 'dbmcget', 'add_minecraft', 'adm_give'] # Сюда добавляй все функции
