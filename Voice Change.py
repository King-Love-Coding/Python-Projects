import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say(
    "Hello. Welcome To The World Of Music. Here You Will See a Wide Range Of Music Instruments. Would you like to proceed?")
engine.runAndWait()

x = input("y/n: ").upper()
if x == 'Y':
    engine.say("Let's Continue")
    engine.runAndWait()

    engine.say("Choose The Element You Want To Know About")
    engine.runAndWait()

    instrument_choice = input(
        "\n1. Piano"
        "\n2. Guitar"
        "\n3. MouthOrgan"
        "\n4. SeaBoard"
        "\nChoose the number corresponding to the instrument: ")

    if instrument_choice == '1':
        engine.say(
            "There Are 5 Types Of Pianos:"
            "\n1. Grand Piano"
            "\n2. Orchestra Piano"
            "\n3. Yamaha Piano"
            "\n4. Electric Piano"
            "\n5. Bass Piano")
        engine.runAndWait()
        piano_choice = input("Choose the piano you want to know further details about: ")

# Further details about the selected piano can be provided here based on the piano_choice

    elif instrument_choice == '2':
        engine.say(
            "There Are 5 Types of Guitars:"
            "\n1. Electric Guitar"
            "\n2. Bass Guitar"
            "\n3. Nylon Guitar"
            "\n4. Ukelele Guitar"
            "\n5. Banjo Guitar")
        engine.runAndWait()
        print(input("There Are 5 Types of Guitars:"
                    "\n1. Electric Guitar"
                    "\n2. Bass Guitar"
                    "\n3. Nylon Guitar"
                    "\n4. Ukelele Guitar"
                    "\n5. Banjo Guitar"))
        guitar_choice = input("Choose the guitar you want to know further details about: ")

        # Further details about the selected guitar can be provided here based on the guitar_choice

        if (guitar_choice == '1'):
            pyttsx3.speak("it is a super Electrifying guitar"
                          ". with modified and strong strings"
                          ". its price range starts from 40000 till 5 lac")
        if (guitar_choice == '2'):
            pyttsx3.speak(
                "it is a super Bass guitar"
                ". with Boost Bass Strings. its price range starts from 60000 till 8 lac")

        if (guitar_choice == '3'):
            pyttsx3.speak("It is an acoustic . wooden guitar . with six nylon guitar strings"
                          ". it is also known as spanish guitar"
                          ". its range starts from 35000 till 12 lack.")
        if (guitar_choice == '4'):
                pyttsx3.speak("it is a small size guitar"
                              ". with soft nylon strings"
                              ". which are gentler on your fingertips"
                              ". and doesn't create finger pain like guitars do"
                              ". its price range starts from 50000 till 10 lac")
        if (guitar_choice == '5'):
                pyttsx3.speak(
                    "it combines the features of the banjo and the guitar"
                    ". it is a versatile instrument . that can be used to play a wide range of music genres"
                    ". its price range starts from 40000 till 10 lac")


    # Add more elif statements for other instruments as needed
    else:
        engine.say("Invalid choice. Please run the program again and choose a valid option.")
        engine.runAndWait()
else:
    engine.say("Thanks For Coming")
    engine.runAndWait()
