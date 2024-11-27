import speech_recognition as sr
from playsound import playsound
from twilio.rest import Client
import geocoder

# Twilio setup
TWILIO_ACCOUNT_SID = 'ACa943f42bc05ae653acacf4b46fa4f8e0'
TWILIO_AUTH_TOKEN = 'e58f9c94a6edb838c3ed541c406107be'
TWILIO_PHONE_NUMBER = '+12564821716'
EMERGENCY_CONTACT = '+919953763198'

# Path to your alarm audio file
ALARM_AUDIO_PATH = 'siren-warning.mp3'

def make_call():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    call = client.calls.create(
        twiml=f'<Response><Play>{ALARM_AUDIO_PATH}</Play></Response>',
        to=EMERGENCY_CONTACT,
        from_=TWILIO_PHONE_NUMBER
    )
    print(f"Call initiated: {call.sid}")

def get_current_location():
    # Use geocoder to get the current location based on IP
    g = geocoder.ipinfo('me')
    if g.ok:
        return f"Latitude: {g.latlng[0]}, Longitude: {g.latlng[1]}"
    else:
        return "Location not available"

def send_sms(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=EMERGENCY_CONTACT
    )

def activate_alarm():
    print("Silent alarm activated!")
    location = get_current_location()
    message = f"Emergency Alert: The alarm has been activated. Current location: {location}."
    send_sms(message)
    make_call()

def listen_for_keyword():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening for activation keyword...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized command: {command}")
        if "help me" in command:
            activate_alarm()
        else:
            print("No activation keyword detected.")
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")

if __name__ == "__main__":
    while True:
        listen_for_keyword()

