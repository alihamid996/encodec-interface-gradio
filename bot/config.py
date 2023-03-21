import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5682718808:AAGco9xNB7tP_dK23otkEP3lDrAe4sO4RF8")

    APP_ID = int(os.environ.get("APP_ID", 9773121))

    API_HASH = os.environ.get("API_HASH", "a367260f49ed27b381ac0da45abcc795")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
