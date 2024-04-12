import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("25853527"))
API_HASH = getenv("7ae0d4b530fa19e2ada9a1c5b811023b")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("6984483844:AAH8X2HvBNF70pb5RMofQF2oCiNDq1awaSw")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6978686334"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Learningbots79/LB_Music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/infinity_bots_support")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/link_frien")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", BQGKflcAcI_uMonE0xsYL2A05f_2amP9oPlIVZ-JkhFP6-B6ZiG5DfspIO8ccjODTrugctVCR3EJLyp54A_4Y_JRm0z36mjkpTZC3ektsS_DEfCfTP3qmCC3dyFJyf6sns1ZteWf8uyACEH_qikD2XMK_jbm2g_FkPpJ7O_PEwLKB1dS2uwOojsnd7za1cIq806-TB9yytbqIRBUpjjd1FDQpYAt2Jak2SdBnL6g6XBiRoc4E7on1fnkcH_NET4ao3w4xxmhDBHyIUbZd5KBZleJ7KUw0zqbBywgr3Cc8Aw0Uu2RpIKIbKVwYORD4MD8H7yDdJ1vlghiGC6QooMqoEbSIUowAAAAGf9k1-AA)
STRING2 = getenv("STRING_SESSION2",BQGKflcAcI_uMonE0xsYL2A05f_2amP9oPlIVZ-JkhFP6-B6ZiG5DfspIO8ccjODTrugctVCR3EJLyp54A_4Y_JRm0z36mjkpTZC3ektsS_DEfCfTP3qmCC3dyFJyf6sns1ZteWf8uyACEH_qikD2XMK_jbm2g_FkPpJ7O_PEwLKB1dS2uwOojsnd7za1cIq806-TB9yytbqIRBUpjjd1FDQpYAt2Jak2SdBnL6g6XBiRoc4E7on1fnkcH_NET4ao3w4xxmhDBHyIUbZd5KBZleJ7KUw0zqbBywgr3Cc8Aw0Uu2RpIKIbKVwYORD4MD8H7yDdJ1vlghiGC6QooMqoEbSIUowAAAAGf9k1-AA)
STRING3 = getenv("STRING_SESSION3",BQGKflcAcI_uMonE0xsYL2A05f_2amP9oPlIVZ-JkhFP6-B6ZiG5DfspIO8ccjODTrugctVCR3EJLyp54A_4Y_JRm0z36mjkpTZC3ektsS_DEfCfTP3qmCC3dyFJyf6sns1ZteWf8uyACEH_qikD2XMK_jbm2g_FkPpJ7O_PEwLKB1dS2uwOojsnd7za1cIq806-TB9yytbqIRBUpjjd1FDQpYAt2Jak2SdBnL6g6XBiRoc4E7on1fnkcH_NET4ao3w4xxmhDBHyIUbZd5KBZleJ7KUw0zqbBywgr3Cc8Aw0Uu2RpIKIbKVwYORD4MD8H7yDdJ1vlghiGC6QooMqoEbSIUowAAAAGf9k1-AA)
STRING4 = getenv("STRING_SESSION4",BQGKflcAcI_uMonE0xsYL2A05f_2amP9oPlIVZ-JkhFP6-B6ZiG5DfspIO8ccjODTrugctVCR3EJLyp54A_4Y_JRm0z36mjkpTZC3ektsS_DEfCfTP3qmCC3dyFJyf6sns1ZteWf8uyACEH_qikD2XMK_jbm2g_FkPpJ7O_PEwLKB1dS2uwOojsnd7za1cIq806-TB9yytbqIRBUpjjd1FDQpYAt2Jak2SdBnL6g6XBiRoc4E7on1fnkcH_NET4ao3w4xxmhDBHyIUbZd5KBZleJ7KUw0zqbBywgr3Cc8Aw0Uu2RpIKIbKVwYORD4MD8H7yDdJ1vlghiGC6QooMqoEbSIUowAAAAGf9k1-AA)
STRING5 = getenv("STRING_SESSION5",BQGKflcAcI_uMonE0xsYL2A05f_2amP9oPlIVZ-JkhFP6-B6ZiG5DfspIO8ccjODTrugctVCR3EJLyp54A_4Y_JRm0z36mjkpTZC3ektsS_DEfCfTP3qmCC3dyFJyf6sns1ZteWf8uyACEH_qikD2XMK_jbm2g_FkPpJ7O_PEwLKB1dS2uwOojsnd7za1cIq806-TB9yytbqIRBUpjjd1FDQpYAt2Jak2SdBnL6g6XBiRoc4E7on1fnkcH_NET4ao3w4xxmhDBHyIUbZd5KBZleJ7KUw0zqbBywgr3Cc8Aw0Uu2RpIKIbKVwYORD4MD8H7yDdJ1vlghiGC6QooMqoEbSIUowAAAAGf9k1-AA)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/e27713b6f830b3314d981.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/bc7f8903e60fbfafa2eb4.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://graph.org/file/2fd73ef39c62047594009.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/6db32c63c677905cc5cc3.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/6db32c63c677905cc5cc3.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
