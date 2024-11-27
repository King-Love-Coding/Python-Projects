import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

Q = input("Lets Play KBC y/n").upper()
if (Q == 'Y'):
    print("Khel Ka Shubharambh Kiya Jaye")
    pyttsx3.speak("Lets Play KBC")

    print("Question 1:Who is the PM of INDIA?")
    pyttsx3.speak("Here  is  your  Question 1:  Who  is  the  PM  of  INDIA?")
    pyttsx3.speak("and your options are:")
    ans = "a Narendra Modi", "b Rahul Gandhi", "c Manmohan Singh", "d Amit Shah"
    print(ans)
    pyttsx3.speak(ans)
    result = input("Your Answer")
    if(result == 'a'):
        print("Aap 1000 Rupee jeet gye hain")
        pyttsx3.speak("You Won 1000 Rupees")

        print("Question 2: Who won the election with the difference of 7 lakh 44 thousand Votes?")
        pyttsx3.speak("Question 2: Who won the election , with the difference of , 7 lakh 44 thousand Votes?")
        pyttsx3.speak("and your options are:")
        ans = "a Akhilesh Yadav", "b Rahul Gandhi", "c Udhaav Thakre", "d Amit Shah"
        print(ans)
        pyttsx3.speak(ans)
        result = input("Your Answer")
        if (result == 'd'):
            print("Aap 5000 Rupee jeet gye hain")
            pyttsx3.speak("You Won 5000 Rupees")

            pyttsx3.speak("Next Question , for 10000 rupees.")

            print("Question 3: Which day is celebrated on 14 february?")
            pyttsx3.speak("Which day is celebrated on 14 february?")
            pyttsx3.speak("and your options are:")
            ans = "a Blue Day", "b Black Day", "c Red Day", "d Green Day"
            print(ans)
            pyttsx3.speak(ans)
            result = input("Your Answer")
            if (result == 'b'):
                print("Aap 10000 Rupee jeet gye hain")
                pyttsx3.speak("You Won 10000 Rupees")
else:
    print("ye jawab galat hai")
    pyttsx3.speak("Sorry Wrong Answer")



