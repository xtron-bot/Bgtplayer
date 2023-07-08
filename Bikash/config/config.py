import os
import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
  load_dotenv("Internal")

API_ID = int(getenv("API_ID", "29875920")
API_HASH = getenv("API_HASH", "61212f0de6f4f30f72bca2f9b9c4751f")
BOT_TOKEN = getenv("BOT_TOKEN", "6329357030:AAF7GuYFDM0_6yfzjTyZHAgfqKwCVkSoSf8")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! ."¡").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://YashKumar:YashKumar@cluster0.jlfgfls.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001848953752")
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "ᴇxᴛʀᴏɴ ᴍᴜꜱɪᴄ </3")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5840343423").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "a254b4a5-d709-4aca-a71f-25a87a643b9d")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "xtron-music")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "github.com/xtron-bot/Bgtplayer")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Panther")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Alone_Vibee")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Alphas_Group")
SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", False)
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQCeBxYyGE9jUnu5TkTH3dPYhdTtRrBZdf2s2gUYYr3Lzih2vAmuigmKLUB5aixJ6uSJ9JfEEW0V-ij3eiaCWsS8W2urSi2OeQjvfp4TbHoHmSDuX5u5S0ieTMJw-Fe7MTBFZvQBZXXq7IrrcQPK1HftFQqTxiR3s_Hl2TiRqVmqGlopmrP3UiFtmyjjSxXWGENCbpdihZHSIhWgVOSn4PRynDRCd8llyCFn_a-KBrOs6nhDLmFh8PjmTadOZmtRgeROxD6KVXLYMv6CM1_Btjc-q9AU_MALPPtC8u5m41cIgs5bWOrl7eCDSD2J7IJMbtMUuhTSXxfQ6egB8pewqNTyAAAAAVCfLYQA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

############################
COMMAND_PREFIXES.append('')
OWNER_ID.append(1439222689)
############################
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
############################

START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/c8135608b7f9f77541a82.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://te.legra.ph/file/3127b3484676bd2254e97.jpg")

PLAYLIST_IMG_URL = "https://te.legra.ph/file/c8135608b7f9f77541a82.jpg"
GLOBAL_IMG_URL = "https://te.legra.ph/file/2e2741f5dfe9f62eed91d.png"
STATS_IMG_URL = "https://te.legra.ph/file/2be94fc76030833b51a78.png"
TELEGRAM_AUDIO_URL = "https://graph.org/file/d68f9ff85714d4dbc6069.png"
TELEGRAM_VIDEO_URL = "https://graph.org/file/d68f9ff85714d4dbc6069.png"
STREAM_IMG_URL = "https://graph.org/file/93882ae5ea01a7bf687b1.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/0d021735560cbf0bb749a.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/4a8cc770a5bea2136bada.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/8427fca139bcbf3c54bcb.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/8427fca139bcbf3c54bcb.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/8427fca139bcbf3c54bcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "resources/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/3127b3484676bd2254e97.jpg"

if START_IMG_URL:
    if START_IMG_URL != "resources/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/c8135608b7f9f77541a82.jpg"
