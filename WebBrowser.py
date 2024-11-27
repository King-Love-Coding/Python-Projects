import webbrowser

import pyttsx3

# #print("Launching Google")
print("1.Google , 2.Youtube , 3.Yahoo , 4.GoogleMap")
choice = input("What you want to open")
if(choice=='1'):
    a = input("What do you want to search")
    webbrowser.open(f"https://www.google.com/search?q={a}")
elif(choice=='2'):
    b = input("What do you want to search")
    webbrowser.open(f"https://www.youtube.com/search?q={b}")
elif(choice=='3'):
    c = input("What do you want to search")
    webbrowser.open(f"https://www.yahoo.com/search?q={c}")
elif(choice=='4'):
    #d = input("Current Location")
    #e = input("Destination")
    h = input("Enter Area")
    #webbrowser.open(f"https://www.google.com/maps/dir/{d}/{e}/?entry=ttu")
    webbrowser.open(f"https://www.google.co.in/maps/search/hotel+near+{h}?entry=ttu")

    #https://www.google.com/maps/place/Sector+3,+Udaipur,+Rajasthan/@24.5746785,73.7209197,15z/data=!3m1!4b1!4m6!3m5!1s0x3967ef5f3481e875:0x561cc756594e03a9!8m2!3d24.5742516!4d73.728662!16s%2Fg%2F1tcycw8p?entry=ttu
#pyttsx3.speak("Launching Google")
#webbrowser.open("www.google.com")


# import wikipedia
# a=input("what do u want to search?")
# ans=wikipedia.summary(a,sentences=2)
# print(ans)
# a=input("what do u want to search? \n")
# b=int(input("how many lines u want?"))
# ans=wikipedia.summary(a,b)
# print (ans)
# pyttsx3.speak(ans)

# import os
# #os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")
# #C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Word
# a = input("what do u want to open \n 1.powerpoint \n 2.excel \n 3.word \n 4.Music")
# if(a=='1'):
#     os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk")
# elif(a=='2'):
#     os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk")
# elif(a=='3'):
#     os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")
# elif(a=='4'):
#     a = input("which song do you want to open?")
#     os.startfile(f"E:\\Songs\\{a}.mp3")