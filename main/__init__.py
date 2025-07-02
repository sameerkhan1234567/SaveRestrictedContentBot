#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("29755489", default=None, cast=int)
API_HASH = config("05e0d957751c827aa03494f503ab54fe", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("BQHGCGEAUrqf_DQ7z1BBCmNwDxE0ZzgxwpOP5F3hcHvYCnujpiUIoUGLXB8Ma08EflyPFHmpO7s12nkSJO6etoUvw8IztUOKEUg-KtIWPPJS-mxfHb2ZjHtz-sEoWRy4ejYiTqBSt23EazLdPFh1jhIfW9ymSEofVzdaetGyA8GO5J8mf9J94kkNmCmsFMOQ6pCtXpyFYfU_gjlSMfrK9szsl_hrHeW2y-YSJv3rHh4cCqvQaqhMdcPQDgvLxYnMqoNR02p5AEdmFaWtOmqGgiZUjR5YxgL2eZPa_5iF-EeMwLi8VVvbqrB3NgZBJi-kLtcwmayosGeFq6HfJOFtS1nOWNfPxgAAAAGK3XtQAA", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("6624738128", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
