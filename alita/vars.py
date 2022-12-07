from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    APP_ID = int(config("APP_ID", default=None))
    API_HASH = config("API_HASH", default=None)
    OWNER_ID = int(config("OWNER_ID", default=1198820588))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default=None))
    DEV_USERS = [int(i) for i in config("DEV_USERS", default="").split()]
    SUDO_USERS = [int(i) for i in config("SUDO_USERS", default="").split()]
    WHITELIST_USERS = [int(i) for i in config("WHITELIST_USERS", default="").split()]
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="alita")
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="DivideSupport")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="DivideProjects")
    ENABLED_LOCALES = [str(i) for i in config("ENABLED_LOCALES", default="en").split()]
    WORKERS = int(config("WORKERS", default=16))
    BOT_USERNAME = ""
    BOT_ID = ""
    BOT_NAME = ""


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "YOUR BOT_TOKEN"
    APP_ID = 6  # Your APP_ID from Telegram
    API_HASH = "d4abfb49dc3eeb1aeb98ae0f581e"  # Your APP_HASH from Telegram
    OWNER_ID = 12345  # Your telegram user id
    MESSAGE_DUMP = 0  # Your Private Group ID for logs
    DEV_USERS = []
    SUDO_USERS = []
    WHITELIST_USERS = []
    DB_URI = "mongodb_url"
    DB_NAME = "alita"
    NO_LOAD = []
    PREFIX_HANDLER = ["!", "/"]
    SUPPORT_GROUP = "SUPPORT_GROUP"
    SUPPORT_CHANNEL = "SUPPORT_CHANNEL"
    ENABLED_LOCALES = ["ENABLED_LOCALES"]
    WORKERS = 8
