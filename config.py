from os import environ 

class Config:
    API_ID = environ.get("API_ID", "22475424")
    API_HASH = environ.get("API_HASH", "5971f827128727176690c7f302ea46e5")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8147844370:AAFVwIdvFCrzboU5Meqq9CbmEDnLhXsRHu4") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
     DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://Karthik:karthik1@cluster0.zwwg6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Karthik")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6795403349').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
