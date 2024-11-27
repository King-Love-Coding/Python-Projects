import pyttsx3


def text_to_audio(file):
    with open(file, "r") as f:
        text = f.read()

    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()


# Use with a text file path
text_to_audio("xyz.txt")
