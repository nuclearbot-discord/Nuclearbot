from modules.bot_funcs.for_funcs import *		
# - Эта хрень нужна мне не удаляй *		
import random		
from random import Random
from firebase import Firebase	
from modules.config import settings
configfb = {
    "apiKey": "AIzaSyC3vGWkRWrBNLuz5YlysXZMZXGy0gT56LA",
    "authDomain": "164893195950.firebaseapp.com",
    "databaseURL": "https://avroraacha.firebaseio.com/",
    "storageBucket": "avroraacha.appspot.com"
}

firebase = Firebase(configfb)
db = firebase.database()


def db_setchance(chance, chid):
    data = {"shans": chance}
    db.child("chances").child(chid).set(data)


def db_getchance(chid):
    all_users = db.child("chances").get()

    for user in all_users.each():
        kkey = user.key()

        if str(kkey) == str(chid):
            a = user.val()
            return a["shans"]
def db_setchannel(iserv, chid):
    data = {'channel':chid}
    db.child("channels").child(iserv).set(data)


def db_getchannel(iserv):
    all_users = db.child("channels").get()

    for user in all_users.each():
        kkey = user.key()

        if str(kkey) == str(iserv):
            a = user.val()
            return a["channel"]


def db_getchannelt(iserv):
    global a
    a=False
    all_users = db.child("channels").get()
    try:
        for user in all_users.each():
            kkey = user.key()

            if str(kkey) == str(iserv):
                a = True
    except:
        a=False
    return a


def onjn(guild2):
    data = {
        "shans": "20",
        "lang": "eng",
        "chat": "True"
    }
    db.child("timeout").child(guild2).set(data)


def onusr(usrid):
    data = {
        "coins": "100",
        "adm": "False"
    }

    db.child("users").child(usrid).set(data)
def conins(usrid, servid):
    data = {
        usrid: "1"
    }

    db.child("lccoins").child(servid).set(data)
def coinsget(idserv):
    global res
    all_usr11 = db.child("lccoins").get()
    for user in all_usr11.each():
        if user.key() == idserv:
            res = user.val()
    return res
def coinsgett(idserv):
    global res
    res=False
    all_usr11 = db.child("lccoins").get()
    for user in all_usr11.each():
        if user.key() == idserv:
            res = True
    return res

#def addadm(idid):
    #data = {
        #"adm": "True"

    #}
    #db.child("adms").child(idid).set(data)

def coninss(usrid, servid,coins):
    data = {
        usrid: coins
    }

    db.child("lccoins").child(servid).set(data)

def addcoint(id, coins):
    ctex = usrgetc(id)
    data = {
        "coins": str(ctex),
        "adm": 'False'

    }
    db.child("users").child(id).set(data)


def dbusrget(id):
    all_usr1 = db.child("users").get()
    usr2 = []
    for user in all_usr1.each():
        print(user.key())
        usr2.append(str(user.key()))
    return str(id) in usr2


def usrgetc(id):
    all_usr11 = db.child("users").get()
    for user in all_usr11.each():
        if str(user.key()) == str(id):
            res = user.val()
    return res


def dbmcget():
    all_acc1 = db.child("accs").get()
    accs2 = []
    for user in all_acc1.each():
        accs2.append(user.key() + ":" + user.val())
    rnd = random.choice(accs2)
    accitog = rnd.split(":")
    return [str(accitog[0]), str(accitog[1])]



def adm_give(id_):
    admins_list = []

    adms = db.child("adms").get()
    for iamadmin in adms.each():
        admins_list.append(str(iamadmin.key()))

    return str(id_) in admins_list


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
def onusr (*a, **b):
    pass
def dbusrget (*a):
    return True
def usrgetc (*a):
    return []
def addcoint (a, b):
    pass
#'''  # Смотри *

__all__ = ['db_setchance', 'db_getchance', 'onjn', 'dbmcget',  'adm_give', 'onusr', 'dbusrget',
           'usrgetc', 'addcoint']  # Сюда добавляй все функции
__ver__ = '0.2.5'


add_module (__name__, __ver__)
