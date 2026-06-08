from dotenv import load_dotenv
from binance.client import Client
import os

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

client = Client(
    API_KEY,
    API_SECRET,
    testnet=True
)