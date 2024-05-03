from twilio.rest import Client

TWILIO_SID = "ACbb2c35cad3e71842e62ae828e8736a04"
TWILIO_AUTH_TOKEN = "6ff9656f00aa9059d28545d5923bcc05"
TWILIO_VIRTUAL_NUMBER = "+14159685399"
TWILIO_VERIFIED_NUMBER = "+916351771513"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
