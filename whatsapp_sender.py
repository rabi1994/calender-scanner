from twilio_config import get_twilio_client, FROM_WHATSAPP

def send_whatsapp_message(to_number, message_body):
    client = get_twilio_client()
    message = client.messages.create(
        from_=FROM_WHATSAPP,
        body=message_body,
        to=f'whatsapp:{to_number}'
    )
    return message.sid
