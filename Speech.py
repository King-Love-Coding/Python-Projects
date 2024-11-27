# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#     print(voice, voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("Hello World !")
#     engine.runAndWait()
#     engine.stop()
# import os
# import webbrowser
# #
# import pyttsx3
# # # import pyaudio
# # #
# # #
# # # def takecommand():
# # #     ram=
# #
# # # recursive function : function call itself
# #
# # # def fact(n):
# # #     if(n==1):
# # #         return(1)
# # #     else:
# # #         return(n*fact(n-1)*)
# #                # 5*fact(4)
# #                # 5*4*fact(3)
# #                # 5*4*3*fact(2)
# #                # 5*4*3*2*fact(1)
# #                # (5*4*3*2*1)
# #
# # # f=1
# # # def fact(n):
# # #     global f
# # #     if(n==1):
# # #         return
# # #     else:
# # #         f=f*n
# # #         n=n-2
# # #         fact(n)
# # #
# # #
# # #
# # # n=int(input("Enter Any number : "))
# # # fact(n)
# # # print("factorial is : ",f)
# # # =============================================================
# #
# # # a=500
# # # def show():
# # #     global a
# # #     a=100
# # #     print("local variable =",a)
# # #     print("global variable =",globals()['a'])
# # # show()
# #
# # # import  sys
# # #
# # # i=1
# # # sys.setrecursionlimit(504)
# # # x=sys.getrecursionlimit()
# # # print("recursive function limit is : ",x)
# # # def show():
# # #     global i
# # #     print(i)
# # #     i=i+1
# # #     show()
# # #
# # # show()
# import wikipedia
import os
import webbrowser

import pyttsx3
import speech_recognition as sr
from wikipedia import wikipedia


def takeCommand():
    ram = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = ram.listen(source)
        print(audio)
        print("Recognizing....")
        query = ram.recognize_google(audio, language="en-in")
    return(query)

while(1):

    query = takeCommand()
    query = query.lower()

    print(f"User said: {query}\n")

    pyttsx3.speak(f"User said: {query}\n")

    if "open google" in query:
        print("What you want to search")
        pyttsx3.speak("What you want to search :  ")
        a = takeCommand()
        webbrowser.open(f"https://www.google.com/search?q={a}")

    elif "open youtube" in query:
        pyttsx3.speak("Youtube Launching")
        print("What you want to search")
        pyttsx3.speak("What you want to search :  ")
        a = takeCommand()
        webbrowser.open(f"https://www.youtube.com/search?q={a}")

    elif "open word" in query:
        pyttsx3.speak("Word Launching")
        webbrowser.open(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")

    elif "chrome" in query:
        pyttsx3.speak("chrome Launching")
        webbrowser.open(r"https://www.chrome.com")

    elif "wikipedia" in query:
        pyttsx3.speak("Wikipedia Launching")
        # a=input("What you want to search")
        # pyttsx3.speak("What you want to search :  ")
        a = takeCommand()
        ans = wikipedia.summary(a,sentences=3)
        print(ans)
        pyttsx3.speak(ans)

    elif "save file" in query:
        a = takeCommand()
        f = open('demo1.txt', 'a')
        f.write(a)
        f.close()
        print("data saved")
        exit()


    else:
        def shutdown_Laptop():
            if os.name == 'nt':
                os.system('shutdown /s /t 0')
                pyttsx3.speak("Shutting Down Laptop")
    # shutdown_Laptop()



