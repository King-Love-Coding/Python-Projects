# i=1
# while(i<=5):
#     print(i, end=",")
#     i = i + 1


# i=5
# while(i>0):
#     print(i,end=",")
#     i=i-1

# n=1234
# sum=0
# while(n>0):
#     r = n % 10
#     sum = sum + r
#     n = n//10
# print(sum)

# n = "1234"       #string banaya
# sum=0
# for i in range(len(n)):
#     sum = sum + int(n[i])     #string ko integer mein convert kiya
# print(sum)

# n = 1234
# r=0
# while(n>0):
#     if(r%2==0):
#         print(sum)

# n=1234
# save=n
# sum=0
# while(n>0):
#     r=n%10
#     sum = sum*10+r
#     n=n//10
# if(sum==save):
#     print("palendrome")
# else:
#     print("Not")

# n=input()
# if(n==n[::-1]):
#     print("yes")
# else:
#     print("not")

# n = input("Enter Mobile Number")
# if(len(n)==10):
#     if(("0"not in n)and("2"not in n)and("4"not in n)and("8"not in n)):
#         sum = 0
#         for data in n:
#             sum = sum+int(data)
#         if(sum>=10):
#             n=str(sum)
#             sum=0
#             for data in n:
#                 sum=sum+int(data)
#         print("unit number=",sum)
#         if(sum in "1,3,5,6,7"):
#             print("perfect Number")
#         else:
#             print("Addition is not good",sum)
#     else:
#         print("Your number has 0,2,4,8")
# else:
#     print("You Entered Wrong Number")

# n = input("Enter Mobile Number")
# if(len(n)==10):
#         sum = 0
#         for data in n:
#             sum = sum+int(data)
#         if(sum>=10):
#             n = str(sum)
#             sum = 0
#             for data in n:
#              sum = sum+int(data)
#         print("unit number=",sum)
#         if(str(sum) in "1,3,5,6,7"):
#             print("perfect Number")
#         else:
#             print("Addition is not good",sum)
# else:
#     print("Entered Wrong")

from random import randint

import pyttsx3

i=1
winner=0
pyttsx3.speak("Enter Your Bet")
amount=int(input("Enter Any Amount"))
while(i<=10):
    a1 = randint(1,5)
    a2 = randint(1,5)
    a3 = randint(1,5)
    if(a1==a2 and a2==a3):
        pyttsx3.speak("You are Winner")
        print("You are Winner")
        amount = amount+10
        winner=winner+1
        total=total+amount
    elif((a1==a2) or(a3==a2 and a2!=a1)or(a1==a3 and a1!=a2)):
        pyttsx3.speak("Ohooooo Best Of Luck For Next Time")
    else:
        pyttsx3.speak("Complete Looser")
        amount=amount-amount*.10
    pyttsx3.speak(f"Your Result is {a1}{a2}{a3}")
    pyttsx3.speak(f"Your {i} Chances Completed remains {10+i}")
    i = i+1
    delattr(2000)

print("Winner Points")