import re
from os import environ
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
     
 
DATABASE_URI = environ.get('DATABASE_URI', "")
DB_URI = environ.get('DB_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
auth_channel = environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('BOT_OWNER_ID', '').split()]
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
PORT = environ.get("PORT", "8080")
PICS = (environ.get('PICS', 'https://telegra.ph/file/65fe86fc02a73f6fcf0ce.jpg')).split()
syd_channel = environ.get('SYD_CHANNEL', '')
SYD_CHANNEL = int(syd_channel) if syd_channel and id_pattern.search(syd_channel) else None
botcracker_chnl = environ.get('BOTCRACKER_CHNL', '')
BOTCRACKER_CHNL = int(botcracker_chnl) if botcracker_chnl and id_pattern.search(botcracker_chnl) else None
