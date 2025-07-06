from twilio.rest import Client
import os

# It's best to use environment variables for security
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

FROM_WHATSAPP = 'whatsapp:+14155238886'  # Twilio sandbox number

def get_twilio_client():
    return Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
