import os
from dotenv import load_dotenv

load_dotenv()

PRODUCT_URL="https://shop.amul.com/en/browse/protein"
PINCODE=os.getenv("PINCODE")

STATE_FILE="automation-state/state.json"
PRODUCT_NAMES=[
    "Amul High Protein Rose Lassi",
    "Amul High Protein Plain Lassi"
]

ENABLE_TWILIO = os.getenv("TWILIO_ENABLE") == "1"