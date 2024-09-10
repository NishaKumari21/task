from twilio.rest import Client

ACCOUNT_SID = 'your_twilio_account_sid'
AUTH_TOKEN = 'your_twilio_auth_token'
FROM_PHONE = 'your_twilio_phone_number'

def send_alert(to_phone, message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(body=message, from_=FROM_PHONE, to=to_phone)
    print(f"Sent message to {to_phone}: {message.sid}")