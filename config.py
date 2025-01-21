import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ROLE_PERMISIONS = list(map(int, os.getenv("ROLE_PERMISIONS").split(",")))
