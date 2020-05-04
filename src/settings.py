import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
DISCORD_TOKEN = ''
COMMAND_PREFIX = ''

try:
    DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
    COMMAND_PREFIX = os.environ['COMMAND_PREFIX']
except KeyError as err:
    print('Environment variable not found:', err)

INITIAL_EXTENSIONS = [
    'cogs.TestCog'
]
