import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5833550185:AAFzUdwF-uiFxIVwzrVS7VepS5GH9tfv0Bk")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 15830858))
    API_HASH = os.environ.get("API_HASH", "2c015c994c57b312708fecc8a2a0f1a6")
    # Get these values from my.telegram.org
    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5468192421").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    #ToDo Forcesubscribe to The Users to use the bot
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001767363693")
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = ""
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 100000
    # watermark file
    DEF_WATER_MARK_FILE = "© @TheTeleRoid"
    SHORT_LINK_API_URL = os.environ.get("SHORT_LINK_API_URL", "https://za.gl/api")
    SHORT_LINK_API_KEY = os.environ.get("SHORT_LINK_API_KEY", "")
    IS_TEAM_DRIVE = os.environ.get("IS_TEAM_DRIVE", False)
    USE_SERVICE_ACCOUNTS = os.environ.get("USE_SERVICE_ACCOUNTS", False)
    INDEX_URL = os.environ.get("INDEX_URL", "https://m.tortoolkit.workers.dev/0:")
    parent_id = os.environ.get("GDRIVE_FOLDER_ID","")
    STRIP_FILE_NAMES = os.environ.get("STRIP_FILE_NAMES","www.1TamilMV.life - |www.1TamilMV.life -|www.1TamilMV.org - |www.1TamilMV.org -|www.1TamilMV.xyz - |www.1TamilMV.xyz -|@MoviesFlixers_DL|@TellyFun_Official|[MM].|[MM]|[MM] -|www_Telugupalaka_com|@MM_New|@MM_Links|@MM_Linkz|www.TamilRockers.ws -|@Animationmovies|HT_BEATS_|-@lubokvideo|@lubokvideo|@english_movieschannel_|@english_movieschannel|@themovies_channel_|@themovies_channel|@telugu_bluray|@TVshows_HD|[Movies Vip]|[CC].|[CC]|@CC_Links.|@CC_Links|@CC_x265.|@CC_x265|@CC.|@CC|@CC_ALL|@CPR_|@CPR|Moviez_India.|Moviez_India")
    CHANNEL_URL = "@fsubcc\n@fsubcc"
    # Sql Database url
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://aio:aio@aio.5z4gxok.mongodb.net/?retryWrites=true&w=majority")
    
