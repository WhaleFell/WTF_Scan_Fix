import os
from pathlib import Path

# basedir = os.path.abspath(os.path.dirname(__file__))
basedir = Path(__file__).resolve().parent.as_posix()


class Config(object):
    ADMIN = "si"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ""


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.db")
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0"
    }


config = {"default": DevConfig}
