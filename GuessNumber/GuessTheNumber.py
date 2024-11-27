# import random
# number = random.randint(1,10)
# for i in range(0,3):
#     user = int(input("guess the number"))
#     if user == number:
#         print("Hurray!!")
#         print(f"you guessed the number right it's {number}")
#         break
# if user != number:
#     print(f"Your guess is incorrect the number is {number}")
#
#
from random import randint

import pygame
from pygame import mixer

comp=randint(1,100)
mixer.init()
mixer.music.load("../Starting.mp3")
mixer.music.play()
n=int(input("In How Many Chances You Found it : "))
i=1
while(i<=n):
    user=int(input(f"Enter {i} Number : "))
    if(user==comp):
        mixer.music.load("../Right.mp3")
        mixer.music.play()
        print(f"You Are Winner You Found it in {i} chances")
        exit()
        delay(5000)
    elif(user<comp):
        mixer.music.load("../Wrong.mp3")
        mixer.music.play()
        print("Pls Select Higher Number")
    else:
        mixer.music.load("../Wrong.mp3")
        mixer.music.play()
        print("Pls Select Smaller Number")
    print(f"Chances Completed {i} Remains Chances {n-i}")
    i=i+1
print(f"You Are Looser {comp}")
