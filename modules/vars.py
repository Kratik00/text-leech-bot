import os

API_ID    = os.environ.get("API_ID", "25017900")
API_HASH  = os.environ.get("API_HASH", "3830600881a164826e60f2806b28e666")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
