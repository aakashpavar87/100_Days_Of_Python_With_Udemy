from twilio.rest import Client

# TWILIO_API_KEY = "gzjy9WeP4sBGKDeteop8oMGRldjla8PM"
# TWILIO_SID = "SKc131e804d0fd986a5b71731493194fa9"

account_sid = 'ACbb2c35cad3e71842e62ae828e8736a04'
auth_token = '6ff9656f00aa9059d28545d5923bcc05'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+14159685399',
  body='Hello There Its First Message',
  to='+916351771513'
)

print(message.sid)
