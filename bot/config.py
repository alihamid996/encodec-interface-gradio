import os

#add your appid bot token and hash you can get them from bot father
class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", ))

    API_HASH = os.environ.get("API_HASH", "")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
