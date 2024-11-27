import sendsms
import twilio
from twilio.rest import Client

# Your Twilio credentials
account_sid = 'ACa943f42bc05ae653acacf4b46fa4f8e0'  # Replace with your Account SID
auth_token = 'e58f9c94a6edb838c3ed541c406107be'    # Replace with your Auth Token

# Create a client
client = Client(account_sid, auth_token)

# Sending the SMS
message = client.messages.create(
    body="Hello !",   # The message you want to send
    from_='+12564821716',         # Your Twilio number (replace with your Twilio number)
    to='+919953763198'             # The recipient's phone number (replace with the recipient's number)
)

# Print the message SID (optional, useful for tracking the message)
print(f"Message sent with SID: {message.sid}")



