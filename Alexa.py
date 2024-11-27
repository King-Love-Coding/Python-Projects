import os
import webbrowser

import PyPDF2
import choice
import read
import reader
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import query
import choice


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass
    return command

def run_alexa():

    command = take_command()

    if 'play' in command:
        song = command.replace('play', '')
        talk('ok baby playing ' + song)
        pywhatkit.playonyt(song)

    elif 'hey' in command:
        talk('Hey Buddy, How Are You')

    elif 'tell' in command:
        talk('i am good, how was your day')

    elif 'day' in command:
        talk('it was boring all day without you')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'lunch' in command:
        talk('ok darling')

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('I am in a relationship with you')

    elif 'love you' in command:
        talk('sorry i Have a boyfriend, Try it with Siri')

    elif 'location' in command:
        # h = https://www.google.com/ma ps/place/Vidhya+Institute+of+Information+Technology/@24.5928876,73.7235936,17z/data=!3m1!4b1!4m6!3m5!1s0x3967e5853c58f791:0x4d0cae9548b1c73c!8m2!3d24.5928876!4d73.7261685!16s%2Fg%2F11clygtyyb?entry=ttu
        webbrowser.open(f"https://www.google.com/maps/place/Vidhya+Institute+of+Information+Technology/@24.5928876,73.7235936,17z/data=!3m1!4b1!4m6!3m5!1s0x3967e5853c58f791:0x4d0cae9548b1c73c!8m2!3d24.5928876!4d73.7261685!16s%2Fg%2F11clygtyyb?entry=ttu")

    elif 'open' in command:

        if 'Google' in command:
            talk('Opening Google')
            a = take_command()
            talk(f"Searching+{a}")
            webbrowser.open(f"https://www.google.com/search?q={a}")

        elif 'YouTube' in command:
            talk('Opening YouTube')
            talk('What do you want to search')
            a = take_command()
            talk(f"Searching+{a}")
            webbrowser.open(f"https://www.youtube.com/search?q={a}")

        elif 'Chrome' in command:
            talk('Opening Chrome')
            talk('What do you want to search')
            a = take_command()
            talk(f"Searching+{a}")
            webbrowser.open(f"https://www.chrome.com/search?q={a}")

        elif 'Google Maps' in command:
            talk('Opening GoogleMaps')
            talk('What do you want to search')
            a = take_command()
            talk(f"Searching+{a}")
            webbrowser.open(f"https://www.maps.google.com")

        elif 'Word' in command:
            talk('Opening Word')
            webbrowser.open(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")

        elif 'Excel' in command:
            talk('Opening Excel')
            webbrowser.open(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")

        elif 'Powerpoint' in command:
            talk('Opening PowerPoint')
            webbrowser.open(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")

        elif 'WhatsApp' in command:
            talk('opening whatsapp')
            webbrowser.open("https://web.whatsapp.com/")

        elif 'vs code' in command:
            talk('Opening vs code')
            webbrowser.open(r"C:\Users\HP\AppData\Local\Programs\Microsoft VS Code\Code.exe")

        elif 'vs studio' in command:
            talk('Opening vs studio')
            webbrowser.open(r"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe")

        elif 'SQL database' in command:
            talk('Opening SQL Database')
            webbrowser.open(r"C:\Program Files (x86)\Microsoft SQL Server Management Studio 20\Common7\IDE\Ssms.exe")

        elif 'my computer' in command:
            talk('Opening My Computer')
            os.startfile(r"C:\Users\HP\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\This PC")

    # elif 'favour' in command:
    #     talk('ok jaan, i will give u some suggestions')
    #     webbrowser.open(f"https://www.google.com/search?q={command}")

    elif 'shutdown' in command:
        if str(os.name) == 'nt':
            talk('shutting down laptop')
            os.system('shutdown /s /t 0')

    else:
        talk('please say the command again')

while True:
    run_alexa()

