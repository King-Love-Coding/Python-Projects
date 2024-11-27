# import itertools
# from itertools import combinations
# import random                            #BRUTE FORCE ATTACK
# import ch
# import char
# import pyautogui
# import itertools
# import random
# import string

# char = "abcdefghijklmnopqrstuvwxyz"
# num = '1234567890'
# # symbols = "@#$%^&*()<>,.?/"'+-/*='
# allchar = list(char)
# allnum = list(num)
# # allsymbols= list[symbols]
# pwd = pyautogui.password("Enter a Password")
# sample_pwd = ""
# while(sample_pwd != pwd):
#     sample_pwd = random.choices(allchar + allnum , k=len(pwd))
#     print("------>"+str(sample_pwd)+"<------")
#     if(sample_pwd==list(pwd)):
#         print("The Password is:"+"".join(sample_pwd))
#         break



# from random import *
# import os
# u_pwd = input("Enter a Password")
# pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#        'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# pw = ""
# while(pw!=u_pwd):
#     pw =""
#     for letters in range(len(u_pwd)):
#         guess_pwd = pwd[randint(0,27)]
#         pw = str(guess_pwd)+str(pw)
#         print(pw)
#         print("Cracking Password.....Please Wait")
#         os.system("cls")
# print("Your Password Is :",pw)



import random
import string
import pyautogui

# Lists for letters, digits, and punctuation
list1 = list(string.ascii_letters)
list2 = list(string.digits)
list3 = list(string.punctuation)

# Prompt user for password
pwd = pyautogui.password("Enter a Password")

# Initialize empty list to store the guessed password
sample_pwd = [""] * len(pwd)

# Continue guessing until the entire password is correct
while "".join(sample_pwd) != pwd:
    for i in range(len(pwd)):
        if sample_pwd[i] == "":
            if pwd[i] in list1:
                guess = random.choice(list1)
                if guess == pwd[i]:
                    sample_pwd[i] = guess
            elif pwd[i] in list2:
                guess = random.choice(list2)
                if guess == pwd[i]:
                    sample_pwd[i] = guess
            elif pwd[i] in list3:
                guess = random.choice(list3)
                if guess == pwd[i]:
                    sample_pwd[i] = guess

    print("Current Guess: " + "".join(sample_pwd))
    print("-" * 30)  # Separator for readability

print("The Password is: " + "".join(sample_pwd))









