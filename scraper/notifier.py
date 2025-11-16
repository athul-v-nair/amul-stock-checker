import os
import requests
from twilio.rest import Client

def notify_whatsapp(message: str):
    if os.getenv("TWILIO_ENABLE") != "1":
        print("Twilio disabled")
        return
    
    client=Client(os.getenv("TWILIO_SID"),os.getenv("TWILIO_TOKEN"))
    client.messages.create(
        from_=os.getenv("TWILIO_FROM"),
        body=message,
        to=os.getenv("WHATSAPP_TO")
    )
    print("Message sent: ",message)