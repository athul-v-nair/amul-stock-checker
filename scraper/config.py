import os
from dotenv import load_dotenv

load_dotenv()

product_url=os.getenv("PRODUCT_URL")
pincode=os.getenv("PIN_CODE")

ENABLE_TWILIO = os.getenv("TWILIO_ENABLE") == "1"