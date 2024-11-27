import pyttsx3
n = int(input("Display multiplication table of? "))
for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")
pyttsx3.speak(f"{n} * {i} = {n*i}")