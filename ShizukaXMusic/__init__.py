from ShizukaXMusic.core.bot import ShizukaBot
from ShizukaXMusic.core.dir import dirr
from ShizukaXMusic.core.git import git
from ShizukaXMusic.core.userbot import Userbot
from ShizukaXMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = ShizukaBot()
pbot = ShizukaBot("ShizukaXMusic", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
