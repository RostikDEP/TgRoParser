from pyrogram import Client, filters
from dotenv import load_dotenv
import os

load_dotenv()
app = Client(name="me_account", api_hash=os.getenv("API_HASH"), api_id=os.getenv("API_ID"))


